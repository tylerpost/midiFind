import unittest
from random import *
from DFA import *
from stringSort import *
from quicksort import *

#Tests for midiFind's algorithms and the midiSong module
#The sorting algorithms never sort arrays > 50 since this is part of the implementation of midiFind
#(if 50+ songs are returned by the substring search then the user did not input a precise enough contour)
class Tests(unittest.TestCase):

    def test_DFA(self):
        #A variety of patterns and texts to test with
        d1  = DFA("rrududr")
        self.assertEqual(d1.search("rrududruuurrududrrurud"),2)
        d2 = DFA("r")
        self.assertEqual(d2.search("rrrrrrrrrr"),10)
        d3 = DFA("urd")
        self.assertEqual(d3.search("uuuuuuuuuudrdruuuudddr"),0)
        txt = "uurududuruuu"
        #A very long text
        for r in range(500):
            txt+="rrr"
        d4 = DFA("dudr")
        self.assertEqual(d4.search(txt),0)
        d5 = DFA("r")
        self.assertEqual(d5.search(txt),1502)

    def test_stringSort(self):
        #Basic test
        songs = [Song("Hey","Hi","",0),Song("Hey","Homie","",0),Song("Hey","Dawg","",0),Song("Hey","Okay","",0),Song("Hey","duh","",0)]
        stringSort(songs,"name")
        for s in range(0, len(songs)-1):
            self.assertTrue(songs[s].name.upper() <= songs[s+1].name.upper())
        stringSort(songs,"artist")
        for s in range(0, len(songs)-1):
            self.assertTrue(songs[s].artist.upper() <= songs[s+1].artist.upper())
        songs2 = []
        #Test with random strings
        for i in range(50):
            songs2.append(Song(chr(randint(0,127))+chr(randint(0,127)),chr(randint(0,127))+chr(randint(0,127)),"",0))
        stringSort(songs2,"name")
        for s in range(0, len(songs2)-1):
            self.assertTrue(songs2[s].name.upper() <= songs2[s+1].name.upper())
        stringSort(songs2,"artist")
        for s in range(0, len(songs2)-1):
            self.assertTrue(songs2[s].artist.upper() <= songs2[s+1].artist.upper())

    def test_quickSort(self):
        #Test with random ints
        songs = []
        for i in range(50):
            songs.append(Song("","","",randint(0,5)))
        quicksort(songs)
        for s in range(0, len(songs)-1):
            self.assertTrue(songs[s].occ <= songs[s+1].occ)
        #Test with identical ints
        songs2 = []
        for i in range(50):
            songs.append(Song("","","",1))
        quicksort(songs)
        for s in range(0, len(songs2)-1):
            self.assertTrue(songs2[s].occ <= songs2[s+1].occ)

        
unittest.main()
