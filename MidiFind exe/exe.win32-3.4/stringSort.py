#3-way quicksort for Songs, by either artist or title
#let -by- be either "title" or "artist"

from midiSong import Song

#Public method, sorts array a by Song attribute by     
def stringSort(a, by): 
    quick3sort(a, 0, len(a)-1, 0, by)

#3-way quicksort of a from lo to hi, sorting by the char at index charIndex and by Song attribute by
def quick3sort(a, lo, hi, charIndex, by):
    if (hi <= lo):
        return
    lt = lo
    i = lo + 1
    gt = hi
    pivot = charAt(getattr(a[lo], by), charIndex)
    while i <= gt:
        t = charAt(getattr(a[i], by), charIndex)
        if t < pivot:
            a[lt],a[i] = a[i],a[lt]
            lt += 1
            i += 1
        elif t > pivot:
            a[gt],a[i] = a[i],a[gt]
            gt -= 1
        else:
            i += 1

    # a[lo..lt-1] < v = a[lt..gt]] < a[gt+1..hi]
    quick3sort (a, lo, lt-1, charIndex, by)
    if pivot >= 0:
        quick3sort (a, lt, gt, charIndex + 1, by)
    quick3sort(a, gt+1, hi, charIndex, by)

#Internal method, turns char into indexable int 
def charAt(string, charIndex):
    if charIndex < len(string): 
        return ord(string[charIndex].upper())#compares letters as "upper" so that they're in alphabetical order, regardless of upper or lower case
    else: #we've passed the end of the string
        return -1

#basic testing
##def main():
##    songs = [Song("Hey","Hi","",0),Song("Hey","Homie","",0),Song("Hey","Dawg","",0),Song("Hey","Okay","",0),Song("Hey","duh","",0)]
##    stringSort(songs,"name")
##    print("Sorted by name:")
##    for s in songs:
##        print(s.name)
##    print("Sorted by arist:")
##    stringSort(songs,"artist")
##    for n in songs:
##        print (n.artist)
##
##main()

