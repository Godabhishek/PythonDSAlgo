def gcd(x,y):

#naive
#find all factors of x
#find all factors of y
#list all common factors
#largest number that appear in the common factor (cf) list

#slightly improved
#scan from 1 to min(x,y) and test if f divides both m and n and add in cf list
    
    cf = []
    for i in range(1,min(x,y)+1):
        if ((x%i) == 0 and (y%i) ==0 ):
            cf.append(i)
    return (cf[-1])


