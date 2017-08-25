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

#Analysis:
#average efficiency = O(n log n)
#worst case efficiency = O(n^2)
#worst-case: 
#1.pivot chosen is either max or min
#2.already sorted out arrat either ascending or descending
#this would split (n-1) elements in one side and empty in another side
#again you are going to sort out (n-1) elements and hence efficiency becomes O(n^2)
#to reduce this possibility, dont choose any fixed strategy to choose pivot element. choose randomly.
#better would be to randomize the complete list once before QuickSort.
#QuickSort is indeed a very fast sorting algorithm which does it in place without a need for another list
#however, QuickSort is not stable , means it doesnt keep the earlier sort order in place while sorting with another attribute like
#in spreadsheet. sorting columnwise
#mergesort and insertionsorts are stable sorts
