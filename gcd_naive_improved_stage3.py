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

    i = min(x,y)

    while( i > 0):
        if ((x%i) == 0 and (y%i) ==0 ):
            return i #gcd
        else:
            i = i-1



