import sys
sys.setrecursionlimit(100000)
import random

def QuickSort (A, l ,r):

    if (r-l) <= 1:
        return ()

    yellow = l+1

    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow = yellow + 1

    (A[l],A[yellow-1])=(A[yellow-1],A[l])

    QuickSort(A,l,yellow-1)
    QuickSort(A,yellow,r)

def randomize(A):
    for i in range(len(A)//2):
        j=random.randrange(0,len(A),1)
        k=random.randrange(0,len(A),1)
        (A[j],A[k])=(A[k],A[j])

