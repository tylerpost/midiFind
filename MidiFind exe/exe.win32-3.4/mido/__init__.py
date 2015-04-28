# -*- coding: utf-8 -*-
"""
MIDI Objects for Python

Mido is a library for working with MIDI messages and ports. It's
designed to be as straight forward and Pythonic as possible.

Creating messages:

    Message(type, **parameters) -- create a new message

Ports:

    open_input(name=None) -- open an input port
    open_output(name=None) -- open an output port
    open_ioport(name=None) -- open an I/O port (capable of both input
                                                and output)

    get_input_names() -- return a list of names of available input ports
    get_output_names() -- return a list of names of available output ports
    get_ioport_names() -- return a list of names of available I/O ports

Parsing MIDI streams:

    parse(bytes) -- parse a single message bytes
                    (any iterable that generates integers in 0..127)
    parse_all(bytes) -- parse all messages bytes
    Parser -- MIDI parser class

Parsing objects serialized with str(message):                                  

    parse_string(string) -- parse a string containing a message
    parse_string_stream(iterable) -- parse strings from an iterable and
                                     generate messages
 
Sub modules:

    ports -- useful tools for working with ports

For more on MIDI, see:

    http://www.midi.org/


Getting started:

    >>> import mido
    >>> m = mido.Message('note_on', note=60, velocity=64)
    >>> m
    <message note_on channel=0, note=60, velocity=64, time=0>
    >>> m.type
    'note_on'
    >>> m.channel = 6
    >>> m.note = 19
    >>> m.copy(velocity=120)
    <message note_on channel=0, note=60, velocity=64, time=0>
    >>> s = mido.Message('sysex', data=[byte for byte in range(5)])
    >>> s.data
    (0, 1, 2, 3, 4)
    >>> s.hex()
    'F0 00 01 02 03 04 F7'
    >>> len(s)
    7

    >>> default_input = mido.open_input()
    >>> default_input.name
    'MPK mini MIDI 1'
    >>> output = mido.open_output('SD-20 Part A')
    >>>
    >>> for message in default_input:
    ...     output.send(message)

    >>> get_input_names()
    ['MPK mini MIDI 1', 'SH-201']
"""
from __future__ import absolute_import
import os
from .backends import Backend
from . import ports, sockets
from .messages import Message
from .messages import parse_string, parse_string_stream, format_as_string
from .parser import Parser, parse, parse_all

__author__ = 'Ole Martin Bjorndalen'
__email__ = 'ombdalen@gmail.com'
__url__ = 'http://mido.readthedocs.org/'
__license__ = 'MIT'
__version__ = '1.1.3'

# Prevent splat import.
__all__ = []

def set_backend(name=None):
    """Set current backend.

    name can be a module name like 'mido.backends.rtmidi' or
    a Backend object.

    If no name is passed, the default backend will be used.

    This will replace all the open_*() and get_*_name() functions
    in top level mido module. The module will be loaded the first
    time one of those functions is called."""

    glob = globals()

    if isinstance(name, Backend):
        backend = name
    else:
        backend = Backend(name, load=False, use_environ=True)
    glob['backend'] = backend

    for name in dir(backend):
        if name.split('_')[0] in ['open', 'get']:
            glob[name] = getattr(backend, name)

set_backend()

del os, absolute_import
