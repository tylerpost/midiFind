import csv
from substringSearch import substringSearch
import time

class Song():
    def __init__(self,  artist,name, occurances):
        self.artist = artist
        self.name = name
        self.occ = occurances

        def getName(self):
            return self.name

        def getArtist(self):
            return self.artist

        def getOcc(self):
            return self.occ




def main():
    songsFound = []
    start = time.time()
    with open("midiTracks.csv", newline = '') as file:
        contents = csv.reader(file)
        for row in contents:
            for i in range(3,len(row)):
                stringsFound = substringSearch(row[i], "rduduuurduuuu")
                if stringsFound > 0:
                    songsFound.append(Song(row[0], row[1], stringsFound))


    for song in songsFound:
        print(song.name, "\t", song.artist, "\t", song.occ)

    end = time.time()
    print( end-start)

main()
