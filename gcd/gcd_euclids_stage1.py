def gcd(x,y):

#naive
#find all factors of x
#find all factors of y
#list all common factors
#largest number that appear in the common factor (cf) list

#slightly improved - stage 1
#scan from 1 to min(x,y) and test if f divides both m and n and add in cf list

# improved - stage 2
#we dont need the list at all. only need largest common factor

#improved - stage 3    
# run the list in reverse order. work backwards

#euclid's algorithm - stage1
#if d divides both x and y, then d would divide x-y also
#assumption x>y ===>
#step1: if x /y then return y
#step2: else gcd(x,y) = gcd (y,x-y)

    #ensure x>y
    if(x<y):
        (x,y)=(y,x)

    #if y divides x, then return y
    if (x % y)==0:
        return y

    #else gcd(x,y)=gcd(y,x-y)
    else:
        diff = x-y
        #diff > y?possible!
        return (gcd(max(y,diff),min(y,diff)))

    while( i > 0):
        if ((x%i) == 0 and (y%i) ==0 ):
            return i #gcd
        else:
            i = i-1



