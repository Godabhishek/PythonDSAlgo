#selection sort and insertion sort are both O(n^2)
#O(n^2) is infeasible for n over 5000
#Among O(n^2) sorts, insertion sort is better than selection sort (advantage in an alreadz sorted list)

#Recursive insertion sort
#efficiency is still O(n^2)

#by default, python has a recursive depth of less than 1000 (997)
#however we can change it to another known limit. for eg, we know if we are limiting
#our input size to less than 5000 then our depth can be set to somewhere close to that point
#here I'm setting it to 10000

import sys
sys.setrecursionlimit(10000)
    
def insertionsort(seq):
    isort(seq,len(seq))

def isort(seq,k):
    if k>1:
        isort(seq,k-1)
        pos = k-1

        while pos>0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos = pos -1

            
