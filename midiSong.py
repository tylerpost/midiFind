import csv
from substringSearch import substringSearch, makeDFA


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




def findSong(contour):
    songsFound = []
    with open("midiTracks.csv", newline = '') as file:
        contents = csv.reader(file)
        for row in contents:
            for i in range(3,len(row)):
                stringsFound = substringSearch(row[i], makeDFA(contour))
                if stringsFound > 0:
                    songsFound.append(Song(row[0], row[1], row[2], stringsFound))
    if len(songsFound) > 0:
        return songsFound
    return None
    

##    for song in songsFound:
##        print(song.name, "\t", song.artist, "\t", song.occ)



