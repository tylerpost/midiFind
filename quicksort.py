#sorts Song array by occurences --> uses getOcc()
import random

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

def quicksort(array):
    random.shuffle(array)
    sort(array, 0, len(array)-1)
    return array

def sort(a, lo, hi):
    if hi <= lo:
        return
    else:
        p = partition(a, lo, hi) #split array
        sort(a, lo, p-1) #recursively sort left half
        sort(a, p+1, hi) #recursively sort right half
    
def partition(a, lo, hi):
    pivot = a[lo].occ #take first item to be pivot
    i = lo+1 #start examining items after the first item
    j = hi
    done = False
    while not done:
        while i <= j and a[i].occ <= pivot:
            i += 1
        while j >= i and a[j].occ >= pivot:
            j -= 1
        if j <= i:
            done = True
        else:
            a[i],a[j] = a[j],a[i] #exchange greater item with lesser item
    a[lo],a[j] = a[j],a[lo] #put partitioning item in place
    return j #return index of partitioning item


##def main():
##    songs = [Song("","","",1),Song("","","",5),Song("","","",3),Song("","","",3),Song("","","",1),Song("","","",5),Song("","","",6)]
##    quicksort(songs)
##    for s in songs:
##        print(s.occ)
##    print("Done")
##    moresongs = [Song("","","",1),Song("","","",5),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1)]
##    quicksort(moresongs)
##    for s in moresongs:
##        print(s.occ)
##    print("Done")
##main()
