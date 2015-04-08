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
    with open("midiTracks.csv", newline = '',encoding = "ISO-8859-1") as file:
        contents = csv.reader(file)
        dfa = makeDFA(contour)
        for row in contents:
            for i in range(3,len(row)):
                stringsFound = substringSearch(row[i], dfa)
                if stringsFound > 0:
                    songsFound.append(Song(row[0], row[1], row[2], stringsFound))
<<<<<<< HEAD
    if len(songsFound) > 0:
#        songsFound = quicksort.quicksort(songsFound)
        return songsFound
    print("No song found")
    return None
=======
        if len(songsFound) > 0:
            return songsFound
        return None
>>>>>>> origin/master
    

##    for song in songsFound:
##        print(song.name, "\t", song.artist, "\t", song.occ)
#Blind Melon - No Rain - SSSSSAAADDDSS
#Green Day - Good Riddance - SSAADDSADDA
#Blink - Adams Song - AADDAADDAAADD
#Beck - Jackass - DASADDDASADADSSADDDS
#durudddurud udurudddurudurrdrrruurduuudddudduudrdruudddduurduruddduudrudurudddudurrdrruurduuddddudduudrdruurddddudurudddurududurudddurudurrdrrruurduuudddudduudrdruudddd
#DASADDDASAD ADASADDDA
