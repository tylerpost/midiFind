from midiSong import Song

def stringSort(a, by):
    N = len(a)
    aux = [0 for x in range(N)]
    sort(a, 0, N-1, 0, by)

def sort(a, lo, hi, d, by):
    R = 256 #ASCII alphabet size
    count = [0 for x in range (R+2)]
    
    for i in range(lo, hi):
        count[ord(getattr(a[i], by)[d] + 2)] += 1
              
    for r in range(0,R+1):
        count[r+1] += count[r]
              
    for i in range (lo, hi):
        aux[count[ord(getattr(a[i], by)[d])+1]] = a[i]
        aux[count[ord(getattr(a[i], by)[d])+1]] += 1

    for i in range (lo, hi):
        a[i] = aux[i-lo]

    for r in range(0,R):
        sort(a, lo + count[r], lo + count[r+1] - 1, d+1)

def main():
    songs = [Song("Hey","Hi","",0),Song("Hey","Homie","",0),Song("Hey","Dawg","",0),Song("Hey","Okay","",0),Song("Hey","duh","",0)]
    stringSort(songs,"name")
    print("Sorted by name:")
    for s in songs:
        print(s.name)
    print("Sorted by arist:")
    stringSort(songs,"artist")
    for n in songs:
        print (n.artist)

main()
