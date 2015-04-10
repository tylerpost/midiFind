#Uses DFAs and the KMT algorithm
#Still figuring out error-handling
#Build DFA from pattern contour using alphabet {u/a,r,d}*
class DFA():
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

    def index(self, char):
        if (char=='r'):
            return 0
        elif ((char=='u')or(char=='a')):
            return 1
        elif (char=='d'):
            return 2
        else:
            return None #GUI does not allow any other character input so no real error handling is required

    def getContour(self): #returns contour/pattern
        return self.contour

    def getDelta(self): #returns array representing state transitions
        return self.delta

    def getM(self): #returns length of dfa (aka index of final state)
        return self.M

def main():
    dfa  = DFA("rrududr")
    print(dfa.search("rrududruuurrududrrurud"))

main()
