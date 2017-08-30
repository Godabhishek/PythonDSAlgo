#further optimization using dynamic programming technique
#follow the orderof dependancies instead of recursion and directly compute and solve
#the dependancies 
#iterative way

fibdyntable = {}
def fib_dyn(n):
    fibdyntable[0] = 0
    fibdyntable[1] = 1

    for i in range(2,n+1):
        fibdyntable[i] = fibdyntable[i-1]+ fibdyntable[i-2]

    return (fibdyntable[n])


#Never compute things twice
#directly filling the table in dependancy order iteratively (dependancies are acyclic)


