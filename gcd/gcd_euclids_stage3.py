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

#euclid's algorithm - stage3
#performance poor in case of big difference between x and y
#if d divides both x and y, then d should divide the reminder of x/y also

    #ensure x>y
    if(x<y):
        (x,y)=(y,x)

    if(x%y) == 0:
        return y
    else:
        return(gcd(y,x%y))#x%y is always < y

    #or using while instead of recursive
    #comment the if,else section of code shown above to work with while
    #instead of recursive and uncomment the following code
    #while(x%y != 0):
    #    (x,y)=(y,x%y)
    #return y
    
    
