#two strings u of length m, and v of length n
#Long common sequence
def findLCS(u,v):#u[0..m-1], v[0..n-1]

    LCS = [[0]*(len(u)+1) for r in range (len(v)+1)]

    #Actually the independant Base item is (0,0)
    #rest all dependant from there unlike in LCW
    #because we have dependancy from down and from left
    #so even bottom row and right coloumn have dependancies starting from
    #(0,0). But adding them will be still be zero. Hence leave it initialized to 0

    for c in range(len(u)-1,-1,-1):
        for r in range(len(v)-1,-1,-1):
            if u[c] != v[r]:
                #LCW[r][c] = 0 for LCW
                LCS[r][c] = max(LCS[r+1][c],LCS[r][c+1])
            else:
                LCS[r][c] = 1 + LCS[r+1][c+1]
    return LCS[0][0]

