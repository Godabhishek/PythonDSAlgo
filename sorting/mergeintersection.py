#combine two sorted lists A and B into C
def merge(A,B): # merge A[0:m],B[0:n]
    (C,m,n) = ([],len(A),len(B))
    (i,j)=(0,0) #current positions in A,B
    
    while (i+j) < (m+n): # m,n is length so 1 more than the offset values i,j
    #i+j is number of elements merged so far

        #if A is empty, copy B into C
        if (i == m):#A is empty
            C.append(B[j])
            j = j+1
        #if B is empty, copy A into C
        elif (j == n):#B is empty
            C.append(A[i])
            i = i+1
        #otherwise, compare first element of A and B and move the smaller
        #of the two into C
        elif (A[i] <= B[j]):#head of A is smaller
            C.append(A[i])
            i = i+1
        elif (A[i] > B[j]):#head of B is smaller
            C.append(B[j])
            j = j+1
        #Repeat the loop until all elements in A and B have been moved into C
    return (C)


#retain only one copy of the duplicate entry and return no single entries
def duplicates(L):
    (C,m,i) = ([],len(L),0)

    while (i+1 < m):
        if (L[i] != L[i+1]):
            i = i+1
        elif L[i] == L[i+1]:
            while(i+1 < m and L[i] == L[i+1]):
                i = i+1
            C.append(L[i])
            i = i+1
    return (C)

def mergeintersection(L,left,right):
    C = mergesort(L,left,right)
    return duplicates(C)

def mergesort(L,left,right):
    if(right - left )<= 1:#base case
        return (L[left:right])

    if(right-left) > 1:#recursive call case
        mid = (left + right) // 2
        A = mergesort(L,left,mid)
        B = mergesort(L,mid,right)  
    return merge(A,B)
