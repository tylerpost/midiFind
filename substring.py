#Find if a substring "pat" exists in a string "txt", returns a boolean
def substring(txt,pat):
    i=j=0
    N=len(txt)
    M=len(pat)
    dfa=makeDFA(pat)
    while (i<N)and(j<M):
        j = dfa[index(txt[i])][j]
        i += 1
    if (j==M):
        return True
    else:
        return False

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
    print substring("suuuuu","d")
    print substring("ssssuuuuususususususudududududdddd","sususususususu")
    print substring("ssssuuuuususususususudududududdddd","susususususu")

