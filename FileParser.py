##MidiFind FileParser library
##Reads Midi tracks from database
##Creates a Melodic Contour for the song represented using Parson's Code

import mido
from mido import midifiles
import string, os, csv


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
            return 'pls'
            #return None

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
        parsonCont = ""
        lastNote = 0
        note = 0
        notes_in_chord = 1.

        for s in track:                         #iterate through every note in the track
            if (type(s) == mido.messages.Message): # avoid meta_MetaMessage
                if (s.__dict__['type'] == 'note_on'):            #avoid control comments
                    
                    if(s.__dict__['time'] == 0): #if we're in the same chord 
                        notes_in_chord += 1                     
                        note += s.__dict__['note'] #add note sum to chord

                    else: #if we are on a new chord 
                        note /= notes_in_chord 
                        notes_in_chord = 1  
                       
                        if (note > lastNote):
                            parsonCont += "u"
                        elif (note < lastNote):
                            parsonCont += "d"
                        elif (note == lastNote):
                            parsonCont += "r"
                        
                        lastNote = note
                        note = s.__dict__['note']
    
        song.addTrack(parsonCont)

    return song




'''
Opens the database 'MIDI FILES' and reads each file
Creates a list that stores a song object for each MidiFile
'''
def createSongList():
    songList = []
    
    for root, dirs, files in os.walk("MIDI FILES"):
        for name in files:
            artist = root.split('\\')[-1]
            #TODO: modify how the artist appears
            fileLoc = root  + "\\" + name
            try:
                print artist, fileLoc
                songList.append(contour(fileLoc, artist))
            except:
                pass #some files throw mido errors, shamefully skip over them
            
    return songList




'''
Writes the songs and all of their information to midiTracks.csv
Artist, Song name, track 1 contour, ... , track n contour
'''
def writeCSV(songList):
    with open('midiTracks.csv', 'wb') as f:
        writer = csv.writer(f)
        for song in songList:
            temp = [song.getArtist(), song.getName()]
            temp.extend(list(song.getTrack(i) for i in range(song.trackCount())))
            temp[:] = (value for value in temp if value != '')
            #print temp
            writer.writerow(temp)
            
            



def main():
    songs = createSongList()

    writeCSV(songs)
    
##      uncomment below for parsons contour of U-D-R
##      i = 1   
##      while(song.getTrack(i) != None):
##        print "Track" , str(i), ": ", song.getTrack(i)
##        i+=1
            








    
    
    






        
            
    
