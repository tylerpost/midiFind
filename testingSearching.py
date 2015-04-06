import midiSong
##searches the database for the following contours
##used songs that most people would know


jayzHKLife = "rduduuurduuuu"
blnk182WMAA = "drurrrrdrurrrrrr"
billyJPianoM = "ddrrdrrurrdd"
SmashMouthAllStar = "rrurdrdurrdurr"
RHCPCalifornication = "rdurdrdurrrrdu"

foundSongs = midiSong.findSong(RHCPCalifornication)

if foundSongs == None:
    print ("no songs found")

else:
    for song in foundSongs:
        print(song.name, "\t", song.artist, "\t", song.occ)
        print (song.fileLocation)
