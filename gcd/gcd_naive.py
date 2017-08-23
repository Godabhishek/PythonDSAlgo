def gcd(x,y):

    fx = []
    for i in range(1,x+1):
        if (x%i) == 0:
            fx.append(i)

    fy = []
    for j in range(1,y+1):
        if (y%j) == 0:
            fy.append(j)

    cf = []
    for f in fx:
        if f in fy:
            cf.append(f)
    return(cf[-1])
