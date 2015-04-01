#Returns the number of occurences of substring "pat" in "txt"
#Non-fuzzy
#Uses DFAs and the KMT algorithm
#Still figuring out error-handling

def substring(txt,pat):
    dfa=makeDFA(pat)
    N=len(txt)
    M=len(pat) #accept state of DFA
    j = 0 #start state of txt in DFA
    occ = 0 #occurences of pat in txt
    for i in range (0,N):
        j = dfa[index(txt[i])][j]
        if (j==M):
            occ = occ + 1
            j = 0 #if substring is found, reset back to first state
    return occ

#Build DFA from pattern "pat" using alphabet {u/a,s,d}*
def makeDFA(pat):
    M = len(pat)
    dfa = [[0 for x in range(M)] for x in range(3)]
    dfa[index(pat[0])][0] = 1
    X = 0
    for j in range(1,M):
        for c in range(0,3):
            dfa[c][j] = dfa[c][X]
        dfa[index(pat[j])][j] = j+1
        X = dfa[index(pat[j])][X]
    return dfa

#Assign index values to characters in alphabet {u/a,s,d}*
def index(char):
    if (char=='s'):
        return 0
    elif ((char=='u')or(char=='a')):
        return 1
    elif (char=='d'):
        return 2
    else:
        print "Invalid character encountered!"

#Testing   
def main():
    print "Start"
    print "Number of \"u\" in \"suuuuu\" should be 5" 
    print substring("suuuuu","u")
    print "Number of \"d\" in \"ssssuuuuususususususudududududdddd\" should be 9" 
    print substring("ssssuuuuususususususudududududdddd","d")
    print "Number of \"asd\" in \"assasdasdasdasasas\" should be 3" 
    print substring("assasdasdasdasasas","asd")
    print "Number of \"dududusss\" in \"dududussddud\" should be 0" 
    print substring("dududussddud","dududusss")
    print "End"

main()
