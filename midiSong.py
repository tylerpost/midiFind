import csv
from DFA import *


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
        dfa = DFA(contour)
        for row in contents:
            for i in range(3,len(row)):
                if songsFound == 50: #limits return list to 50 songs
                    break
                stringsFound = dfa.search(row[i])
                if stringsFound > 0:
                    songsFound.append(Song(row[0], row[1], row[2], stringsFound))
    if len(songsFound) > 0:
        return songsFound
    print("No song found")
    return None

def main():
    print("Begin")
    songs = findSong("rurrrdrrurrdrurrrdud")
    for s in songs:
        print(s.name)
    print(len(songs))
    
main()

#BARBIE GIRL
#rurrrdrrurrdrurrrdudurrdrrurrdudurrdrurrdrurrdudrrduuuuuuduuduuduuuudruuduuduuuudruududuuuuuduuduuduuuuduuduuduuuudruuduuduuuudduududuuuuuduuuduuduuuuduuduuduuuuuduuduuduuuudduududuuuuuduuduuduuuuduududuuuuuduuduuduuuuduuuduuduuuuuuduuuuduuuduuuuduududduuuudruuduudduudruurdduuuuuduududduuuduududduuuudruududduuudduurdduuuuuduududduuuduududduuuuuduududduuudduudduuuuuduududduuuduurdduuuuuduududduuuduuurdduuuuuuduuuduudduuuuuddddurrduuuurdurrduuudurduuudrduuuurdurrduuurrdurrduuuurdurduuurrdurrduuuurdurduuurrduuudrduuururdduururduuudrurduuuuuuduuduuduuuudruuduuduuuudruududuuuuuduuduuduuuuduuduuduuuudruuduuduuuudduududuuuuuduuuduuduuuuduuduuduuuuuduuduuduuuudduududuuuuuduuduuduuuuduududuuuuuduuduuduuuuduuuduuduuuuuuduuuuduuuduuuuduududduuuudruuduudduudruurdduuuuuduududduuuduududduuuudruududduuudduurdduuuuuduududduuuduududduuuuuduududduuudduudduuuuuduududduuuduurdduuuuuduududduuuduuurdduuuuuuduuuduudduuuuuuduuduuduuudruuduuduuuudruududuuuuduuduuduuuuduuduuduuudruuduuduuuudduududuuuuduuuduuduuuuduuduuduuuuduuduuduuuudduududuuuuduuduuduuuuduududuuuuduuduuduuuuduuuduuduuuuuduuuuduuuduuuuduududduuudruuduudduudruurdduuuuduududduuuduududduuudruududduuudduurdduuuuduududduuuduududduuuuduududduuudduudduuuuduududduuuduurdduuuuduududduuuduuurdduuuuuduuuduudduuuuuddudduuudrduuuurdurrduuurrdurrduuuurdurrduuurrdurrduuuurdurrduuurrdurrduuuurdurrduuurrdurrduuuurdurrduuurrdurrduuuurdurrduuurrdurduuuurdurrduuurrdurrduuuurdurrduuudurduuudrduuuurdurrduuurrdurrduuuurdurduuurrdurrduuuurdurduuurrduuudrdururdduururdudrurduuuururdururdrurdrdurdururdururdrurdududduududuururdururdrurdrdurdururduurdrdurdrruurduduudduduuuuuuduuduuduuuudruuduuduuuudruududuuuuuduuduuduuuuduuduuduuuudruuduuduuuudduududuuuuuduuuduuduuuuduuduuduuuuuduuduuduuuudduududuuuuuduuduuduuuuduududuuuuuduuduuduuuuduuuduuduuuuuuduuuuduuuduuuuduududduuuudruuduudduudruurdduuuuuduududduuuduududduuuudruududduuudduurdduuuuuduududduuuduududduuuuuduududduuudduudduuuuuduududduuuduurdduuuuuduududduuuduuurdduuuuuuduuuduudduuuuuuduuduuduuuudruuduuduuuudruududuuuuuduuduuduuuuduuduuduuuudruuduuduuuudduududuuuuuduuuduuduuuuduuduuduuuuuduuduuduuuudduududuuuuuduuduuduuuuduududuuuuuduuduuduuuuduuuduuduuuuuuduuuuduuuduuuuduududduuuudruuduudduudruurdduuuuuduududduuuduududduuuudruududduuudduurdduuuuuduududduuuduududduuuuuduududduuudduudduuuuuduududduuuduurdduuuuuduududduuuduuurdduuuuuuduuuduudduuuuuuduuduuduuudruuduuduuuudruududuuuuduuduuduuuuduuduuduuudruuduuduuuudduududuuuuduuuduuduuuuduuduuduuuuduuduuduuuudduududuuuuduuduuduuuuduududuuuuduuduuduuuuduuuduuduuuuuduuuuduuuduuuuduududduuudruuduudduudruurdduuuuduududduuuduududduuudruududduuudduurdduuuuduududduuuduududduuuuduududduuudduudduuuuduududduuuduurdduuuuduududduuuduuurdduuuuuduuuduudduuduu

##    for song in songsFound:
##        print(song.name, "\t", song.artist, "\t", song.occ)
#Blind Melon - No Rain - SSSSSAAADDDSS
#Green Day - Good Riddance - SSAADDSADDA
#Blink - Adams Song - AADDAADDAAADD
#Beck - Jackass - DASADDDASADADSSADDDS
#durudddurud udurudddurudurrdrrruurduuudddudduudrdruudddduurduruddduudrudurudddudurrdrruurduuddddudduudrdruurddddudurudddurududurudddurudurrdrrruurduuudddudduudrdruudddd
#DASADDDASAD ADASADDDA
