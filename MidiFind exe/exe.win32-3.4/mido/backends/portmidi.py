"""
Input and Output ports for PortMidi.

There is no need to use this module directly. All you need is
available in the toplevel module.

PortMidi documentation:
http://portmedia.sourceforge.net/portmidi/doxygen/
"""
import time
import threading
from collections import deque
from ..parser import Parser
from ..messages import Message
from ..ports import BaseInput, BaseOutput
from . import portmidi_init as pm

def _check_error(return_value):
    """Raise IOError if return_value < 0.

    The exception will be raised with the error message from PortMidi.
    """
    if return_value < 0:
        raise IOError(pm.lib.Pm_GetErrorText(return_value))
    
    
def _get_device(device_id):
    device = {}
    
    info_pointer = pm.lib.Pm_GetDeviceInfo(device_id)
    if not info_pointer:
        raise IOError('PortMidi device with id={} not found'.format(
            device_id))
    info = info_pointer.contents
     
    return {
        'id': device_id,
        'interface': info.interface.decode('utf-8'),
        'name': info.name.decode('utf-8'),
        'is_input': info.is_input,
        'is_output': info.is_output,
        'opened': bool(info.opened),
    }


def _get_default_device(get_input):
    if get_input:
        device_id = pm.lib.Pm_GetDefaultInputDeviceID()
    else:
        device_id = pm.lib.Pm_GetDefaultOutputDeviceID()
        
    if device_id < 0:
        raise IOError('no default port found')
    
    return _get_device(device_id)


def _get_named_device(name, get_input):
    # Look for the device by name and type (input / output)
    for device in get_devices():
        if device['name'] != name:
            continue

        # Skip if device is the wrong type
        if get_input:
            if device['is_output']:
                continue
        else:
            if device['is_input']:
                continue

        if device['opened']:
            raise IOError('port already opened: {!r}'.format(name))

        return device
    else:
        raise IOError('unknown port {!r}'.format(name))


def get_devices(**kwargs):
    """Return a list of devices as dictionaries."""
    return [_get_device(i) for i in range(pm.lib.Pm_CountDevices())]


class PortCommon(object):
    """
    Mixin with common things for input and output ports.
    """
    def _open(self, **kwargs):
        self._stream = pm.PortMidiStreamPtr()

        opening_input = hasattr(self, 'receive')

        if self.name is None:
            device = _get_default_device(opening_input)
            self.name = device['name']
        else:
            device = _get_named_device(self.name, opening_input)

        if device['opened']:
            if opening_input:
                devtype = 'input'
            else:
                devtype = 'output'
            raise IOError('{} port {!r} is already open'.format(devtype,
                                                                self.name))
        
        if opening_input:
            _check_error(pm.lib.Pm_OpenInput(
                         pm.byref(self._stream),
                         device['id'],  # Input device
                         pm.null,       # Input driver info
                         1000,          # Buffer size
                         pm.NullTimeProcPtr,  # Time callback
                         pm.null))      # Time info
        else:
            _check_error(pm.lib.Pm_OpenOutput(
                         pm.byref(self._stream),
                         device['id'],  # Output device
                         pm.null,       # Output diver info
                         0,             # Buffer size
                                        # (ignored when latency == 0?)
                         pm.NullTimeProcPtr,  # Default to internal clock
                         pm.null,       # Time info
                         0))            # Latency

        # This is set when we return, but the callback thread needs
        # it to be False now (or it will just return right away.)
        self.closed = False
        

        if opening_input:
            if self.callback:
                self._callback_thread = threading.Thread(
                    target=self._thread_main)
                self._callback_thread.daemon = True
                self._callback_thread.start()

                # Make sure pending() doesn't see messages.
                self._messages = deque()

        self._device_type = 'PortMidi/{}'.format(device['interface'])

    def _close(self):
        _check_error(pm.lib.Pm_Close(self._stream))

class Input(PortCommon, BaseInput):
    """
    PortMidi Input port
    """
    def _read(self):
        # I get hanging notes if MAX_EVENTS > 1, so I'll have to
        # resort to calling Pm_Read() in a loop until there are no
        # more pending events.
        max_events = 1

        # Todo: this should be allocated once
        BufferType = pm.PmEvent * max_events
        read_buffer = BufferType()

        # Read one message. Should return 1.
        # If num_events < 0, an error occured.
        length = 1  # Buffer length
        num_events = pm.lib.Pm_Read(self._stream, read_buffer, length)
        _check_error(num_events)
        
        # Get the event
        event = read_buffer[0]
        # print('Received: {:x}'.format(event.message))

        # The bytes of the message are stored like this:
        #    0x00201090 -> (0x90, 0x10, 0x10)
        # (Todo: not sure if this is correct.)
        packed_message = event.message & 0xffffffff
        
        for i in range(4):
            byte = packed_message & 0xff
            self._parser.feed_byte(byte)
            packed_message >>= 8

    def _receive(self, block=True):
        if self.callback:
            raise IOError('a callback is currently set for this port')
        
        if block:
            while not self._messages:
                self._read()
        else:
            while pm.lib.Pm_Poll(self._stream):
                self._read()

    def _thread_main(self):
        # Todo: exceptions do not propagate to the main thread, so if
        # something goes wrong here there is no way to detect it, and
        # there is no warning. (An unknown variable, for example, will
        # just make the thread stop silently.)
        while not self.closed:
            try:
                self._read()
            except IOError:
                if self.closed:
                    # If the port is closed (and _check_error() works),
                    # "IOError: PortMidi: `Bad pointer'" is raised
                    # if the port is closed in self._read().
                    # Just exit. (Basically, ignore errors if the port is
                    # closed.)
                    break
                else:
                    raise

            for message in self._parser:
                if self.callback:
                    self.callback(message)

    def _close(self):
        self.callback = False
        PortCommon._close(self)

class Output(PortCommon, BaseOutput):
    """
    PortMidi output port
    """

    def _send(self, message):
        if message.type == 'sysex':
            # Sysex messages are written as a string.
            string = pm.c_char_p(bytes(message.bin()))
            timestamp = 0  # Ignored when latency = 0
            _check_error(pm.lib.Pm_WriteSysEx(self._stream, timestamp, string))
        else:
            # The bytes of a message as packed into a 32 bit integer.
            packed_message = 0
            for byte in reversed(message.bytes()):
                packed_message <<= 8
                packed_message |= byte

            timestamp = 0  # Ignored when latency = 0
            _check_error(pm.lib.Pm_WriteShort(self._stream,
                                              timestamp,
                                              packed_message))
