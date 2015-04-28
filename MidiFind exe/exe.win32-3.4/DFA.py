#Performs substring search using DFAs and the KMT algorithm
#Returns number of substring occurrences in string
class DFA():
    #Build transition states array from pattern/contour using alphabet {u/a,r,d}*
    def __init__(self, pat):
        self.M = len(pat)
        self.contour = pat
        self.delta = [[0 for x in range(self.M)] for x in range(3)]
        self.delta[self.index(pat[0])][0] = 1
        X = 0
        for j in range(1,self.M):
            for c in range(0,3):
                self.delta[c][j] = self.delta[c][X]
            self.delta[self.index(pat[j])][j] = j+1
            X = self.delta[self.index(pat[j])][X]

    #Search for substring in txt. Returns number of occurrences of substring in text.
    def search(self, txt):
        N=len(txt)
        j = 0 #start state of txt in DFA
        occ = 0 #occurences of pat in txt
        for i in range (0,N):
            j = self.delta[self.index(txt[i])][j]
            if (j==self.M):
                occ = occ + 1
                j = 0 #if substring is found, reset back to first state
        return occ

    #Internal method, maps each character in the alphabet to an int that may be used as an array index.
    def index(self, char):
        if (char=='r'):
            return 0
        elif ((char=='u')or(char=='a')):
            return 1
        elif (char=='d'):
            return 2
        else:
            return None #GUI does not allow any other character input so no real error handling is required

    #Getters, for testing mostly
    #Returns contour/pattern
    #(not really used, but it could be helpful to know the pattern that is associated with the DFA)
    def getContour(self): 
        return self.contour

    #Returns array of transition states
    def getDelta(self): #returns array representing state transitions
        return self.delta

    #Returns length of dfa(index of final/accept state)
    def getM(self):
        return self.M

    #No setters --> Immutable

#basic testing
##def main():
##    d1  = DFA("rrududr")
##    print("rrududr appears 2 times in rrududruuurrududrrurud")
##    print(d1.search("rrududruuurrududrrurud"))
##    d2 = DFA("r")
##    print("r appears 10 times in rrrrrrrrrr")
##    print(d2.search("rrrrrrrrrr"))
##    d3 = DFA("urd")
##    print("urd appears 0 times in uuuuuuuuuudrdruuuudddr")
##    print(d3.search("uuuuuuuuuudrdruuuudddr"))
##
##main()
