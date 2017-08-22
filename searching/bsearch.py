
def search (seq,v,l,r):
#seq from [l:r]; seq is sorted;
#only for arrays its possible, but not for lists
#time taken is log(r). for eg: if seq is 1000 entries, it needs 10 steps (2^10 = 1024) to complete a search
#efficency --> O(log n)
#input of size - log n
# 10 - 3.3
# 100 - 6.6
# 1000 - 10
# 10^7 - 23
# 10^10 - 33
# as you see this one is efficient even for input of size 10^10

    if( r -l == 0):
        return False

    mid = (l + r) // 2

    if ( v == seq[mid]):
        return True
    
    elif (v < seq[mid]):
        return search(seq,v,l,mid)

    else:
        return search(seq,v,mid+1,r)

