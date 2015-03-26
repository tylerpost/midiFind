##MidiFind FileParser library
##Reads Midi tracks from database
##Creates a Melodic Contour for the song represented using Parson's Code

import mido
from mido import midifiles
import string
import os

'''
Used to store Melodic Contours of each song
getTrack() returns None if there is no n'th track for that song
'''
class Song():
    def __init__(self, name, artist):
        self.artist = artist
        self.name = name
        self.tracks = []

    def getName(self):
        return self.name;

    def getArtist(self):
        return self.artist

    ##tracks[0] is empty? confirm for other songs.
    def getTrack(self,n):
        try:
            return self.tracks[n]
        except:
            return None

    def addTrack(self, track):
        self.tracks.append(track)

    def trackCount(self):
        return len(self.tracks)


'''
Takes as input midiFile in the format "songName.mid"
Generates a Melodic Contour for each track
Passes back a new song object
'''
def contour(midiFile, artist):
    name = midiFile.split('\\')[-1]
    song = Song(name.strip(".mid"), artist)

    midiSong = mido.midifiles.MidiFile(midiFile)

    for i, track in enumerate(midiSong.tracks): #iterate through every track
        #track.name
        parsonCont = ""
        lastNote = 0
        note = 0
        notes_in_chord = 1.
        

        for s in track:                         #iterate through every note in the track
            if (type(s) == mido.messages.Message): # avoid meta_MetaMessage
                s = mido.messages.format_as_string(s)
##                print s
                if (s[0:7] == "note_on"):            #avoid control comments
                    
                    if(int(s[(s.index("time=") + 5):]) == 0): #if we're in the same chord 
                        notes_in_chord += 1                     
##                        print note
                        note += int(s[(s.index("note=") + 5): s.index("velocity=")]) #add note sum to chord
                        
##                        note /= notes_in_chord
##                        print note
                        #divide by total notes in the chord
##                        print note, "\t", notes_in_chord
                    else: #if we are on a new chord 
                        notes_in_chord = 1  
                       
                        if (note > lastNote):
                            parsonCont += "u"
                        elif (note < lastNote):
                            parsonCont += "d"
                        elif (note == lastNote):
                            parsonCont += "r"
                        
                        lastNote = note
##                        print "note written with: ,", note
                        note = int(s[(s.index("note=") + 5): s.index("velocity=")])
    
        song.addTrack(parsonCont)

    return song




'''
Opens the database 'MIDI FILES' and reads each file
Creates a list that stores a song object for each MidiFile
'''
def database():
    songList = []
    badfile = 0
    qty = 10
    
    for root, dirs, files in os.walk("MIDI FILES\Pearl Jam"):
        for name in files:
            artist = root.split('\\')[-1]
            #TODO: modify how the artist appears
            fileLoc = root  + "\\" + name        

            try:
                songList.append(contour(fileLoc, artist))
            except:
                pass #some files throw mido errors, shamefully skip over them
            
    return songList





def main():
    songs = database()
    for song in songs:
      print song.getName(), "\t", song.getArtist()
##      uncomment below for parsons contour of U-D-R
##      i = 1   
##      while(song.getTrack(i) != None):
##        print "Track" , str(i), ": ", song.getTrack(i)
##        i+=1
            
        








    
    
    






        
            
    
