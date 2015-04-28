##Opens and reads CSV database
##midiTracks.csv must be inside local folder
##Returns a list of Songs matching contours

import csv
from DFA import *


'''
Construct song object that holds attributes required to identify it
'''
class Song():
    def __init__(self,  artist,name,fileLoc, occurances):
        self.artist = artist
        self.name = name
        self.fileLocation = fileLoc
        self.occ = occurances

        def getName(self):
            return self.name

        def getArtist(self):
            return self.artist

        def getFileLoc(self):
            return self.fileLocation

        def getOcc(self):
            return self.occ


'''
Opens the database midiTracks.csv and calls DFA.search on every track in the csv
If a track has been found, create a Song instance
Once the contour has been passed, or too many results are found, return the list of matching Songs
'''
def findSong(contour):
    songsFound = []
    with open("midiTracks.csv", newline = '',encoding = "ISO-8859-1") as file:
        contents = csv.reader(file)
        dfa = DFA(contour)
        for row in contents:
            for i in range(3,len(row)):
                if len(songsFound) == 50: #limits return list to 50 songs
                    return songsFound
                stringsFound = dfa.search(row[i])
                if stringsFound > 0:
                    songsFound.append(Song(row[0], row[1], row[2], stringsFound))
    if len(songsFound) > 0:
        return songsFound
    return None


##Some tracks that can be found inside the database with the following contours:
#BARBIE GIRL rurrrdrrurrdrurrrd
#Blind Melon - No Rain - SSSSSAAADDDSS
#Green Day - Good Riddance - SSAADDSADDA
#Blink - Adams Song - AADDAADDAAADD
#Beck - Jackass - DASADDDASADADSSADDDS

