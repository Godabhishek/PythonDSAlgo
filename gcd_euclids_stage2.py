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

#euclid's algorithm - stage2
#replace recursive with while

    #ensure x>y
    if(x<y):
        (x,y)=(y,x)

    #loop until y is divided by x or y=1
    while (x % y)!=0:
        diff = x-y
        #diff > y?possible!
        (x,y)=(max(y,diff),min(y,diff))

    return y
