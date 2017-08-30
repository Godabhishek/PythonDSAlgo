def fib(n):
    if n <= 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fib(n-1)+fib(n-2)

    return value

#naive way as the computation of sub-problems are redundant. wasteful recomputation though
#we get an answer from the earlier computation.. exponentially growing sub-problems
#so try to remember the answers from subproblems computed and use the answer from the
#memory table
#memoization
fibtable ={}

def fib_mem(n):
    try:
        if fibtable[n]:
            print('from mem_table','n=',n, fibtable[n])
            return (fibtable[n])
    except KeyError:
        if n <= 0:
            value = 0
        elif n == 1:
            value = 1
        else:
            value = fib_mem(n-1)+fib_mem(n-2)
        fibtable[n] = value

    return value

