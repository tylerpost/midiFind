#sorts Song array by occurences --> uses getOcc()
import random
def quicksort(array):
    random.shuffle(array)
    sort(array, 0, len(array)-1)

def sort(a, lo, hi):
    if hi <= lo:
        return
    p = partition(a, lo, hi) #split array
    sort(a, lo, p-1) #recursively sort left half
    sort(a, p+1, hi) #recursively sort right half
    
def partition(a, lo, hi):
    pivot = a[lo].getOcc() #take first item to be pivot
    i = lo+1 #start examining items after the first item
    j = hi
    done = False
    while not done:
        while a[i].getOcc() < pivot and i < hi:
            i += 1
        while a[j].getOcc() > pivot and j > lo:
            j -= 1
        if j <= i:
            done = True
        else:
            a[i],a[j] = a[j],a[i] #exchange greater item with lesser item
    a[lo],a[j] = a[j],a[lo] #put partitioning item in place
    return j #return index of partitioning item
