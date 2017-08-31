#two strings u of length m, and v of length n
#subword of length 'k'
#first find  legth of common word i.e., K and
#then you can dtermine the common word as a byproduct

#LCW (m,j) = 0 for all j. we have reached 'm' or end of 1st string
#LCW (i,n) = 0 for all i. we have reached 'n' or end of 2nd string
#if u(i) != v(j) LCW (i,j) = 0 
#else LCW (i,j) = 1 + LCW (i+1,j+1)

#dependancy is from the higher level to lower level unlike in grid problem
#(i,j) depends on (i+1,j+1)


def findLCW(u,v):
    
    LCW = [[0]*(len(u)+1) for r in range (len(v)+1)]

#following is the base class where last column and last row are equal to zero
#however its commented out here as it is taken care in the init phase above
##    for r in range(len(u)+1):
##        LCW[r][len(v)+1] = 0
##    for c in range(len(v)+1):
##        LCW[len(u)+1][c] = 0

    MAXLCW = 0
                
    for c in range(len(u)-1,-1,-1):
        for r in range(len(v)-1,-1,-1):
            if u[c] != v[r]:
                LCW[r][c] = 0
            else:
                LCW[r][c] = 1 + LCW[r+1][c+1]
            if (LCW[r][c] > MAXLCW):
                MAXLCW = LCW[r][c]

    #ugly solution but will be corrected later
    for c in range(0,len(u)):
        for r in range(0,len(v)):
            if LCW[r][c] == MAXLCW:
                i = r
                j = c
                subword = ""
                while(LCW[i][j] > 0):
                    subword += u[j]
                    i += 1
                    j += 1
                print(subword)
    return MAXLCW

