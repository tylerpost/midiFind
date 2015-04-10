#sorts Song array by occurences --> uses Song.occ
import random, sys
sys.setrecursionlimit(100)
from midiSong import Song

def quicksort(a):
    random.shuffle(a)
    sort(a, 0, len(a)-1)
    return a

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
        if i >= j:
            done = True
        else:
            a[i],a[j] = a[j],a[i] #exchange greater item with lesser item
    a[lo],a[j] = a[j],a[lo] #put partitioning item in place
    return j #return index of partitioning item

##
##def main():
##    songs = [Song("","","",1),Song("","","",5),Song("","","",3),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1),Song("","","",1)]
##    quicksort(songs)
##    for s in songs:
##        print(s.occ)
##    print("Done")
##main()
