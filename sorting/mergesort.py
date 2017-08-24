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
#merge function analysis:
#size of C is m+n added one element in one iteration
#m+n <= 2 max(m,n) and we have chosen in such a way we are dividing the list into two halves of roughly the same size
#, hence m ~ n
#hence O(max(m,n)) = O(n) and hence this function is linear in input size

def mergesort(L,left,right):
    if(right - left )<= 1:#base case
        return (L[left:right])

    if(right-left) > 1:#recursive call case
        mid = (left + right) // 2
        A = mergesort(L,left,mid)
        B = mergesort(L,mid,right)

    return (merge(A,B))

    
#merge sort creates a new array C and returns the new one, but it doesnt modify the original array
#or this is not effectively merged in place
#extra storage is costly based on the input size

#mergesort analysis
#we are dividing the list into two equal lists and assume the input n is properly divided by 2. hence n = 2^k
#T(n) = 2 T(n/2) + n (from merge function) [expand]
#T(n) = 2 [ 2 T(n/4) + n/2] + n = 2^2 T(n/2^2) + 2n
#further on..... after j steps
#in general: 2^j T(n/2^j) + jn 
#base case is T(1)-> when j = log(base 2)n , (n/2^j) = 1, so T(n/2^j)=1
#After log n steps:
#T(n) = 2^log n *1 + (log n)n
#2^log n --> n by definition
#hence T(n) = n + n logn = O(n log n)#considering the higher term
#hence efficiency is O(n log n)
#efficiency - n log n
