def stringSort(array): #3-way quicksort for strings
    quick3sort(array, 0, len(array)-1, 0)

def quick3sort(a, lo, hi, charIndex):
    if (hi <= lo):
        return
    lt = lo
    i = lo + 1
    gt = hi
    pivot = charAt(a[lo], charIndex)
    while i <= gt:
        t = charAt(a[i], charIndex)
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
    quick3sort (a, lo, lt-1, charIndex)
    if pivot >= 0:
        quick3sort (a, lt, gt, charIndex + 1)
    quick3sort(a, gt+1, hi, charIndex)

def charAt(string, charIndex):
    if charIndex < len(string): 
        return ord(string[charIndex]) #turns char into comparable int
    else: #we've passed the end of the string
        return -1

def main():
    a = ["hi","hello","apple","banana","apples"]
    stringSort(a)
    print a

main()
