
# Python 3 program to calculate 
# Euler's Totient Function 
# using Euler's product formula 
  
def phi(n) : 
  
    result = n   # Initialize result as n 
       
    # Consider all prime factors 
    # of n and for every prime 
    # factor p, multiply result with (1 - 1 / p) 
    p = 2
    while(p * p<= n) : 
  
        # Check if p is a prime factor. 
        if (n % p == 0) : 
  
            # If yes, then update n and result 
            while (n % p == 0) : 
                n = n // p 
            result = result * (1.0 - (1.0 / (float) (p))) 
        p = p + 1
          
          
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most one 
    # such prime factor) 
    if (n > 1) : 
        result = result * (1.0 - (1.0 / (float)(n))) 
   
    return (int)(result)


keepgoing = True
startvalue = 2
endvalue = 1000000000
desiredvalue = 15499/94744
print(desiredvalue)
margin = 1/10

# This method is not really working as the resilience does not get closer to the
# the desired value in a linear way.

##while keepgoing == True:
##    guess = (int) ((startvalue + endvalue)/2)
##    result = phi(guess)/(guess-1)
##    difference = desiredvalue - result
##    absdif = abs(difference)
##    print ('Guess: ' + str(guess))
##    print('Resilience: ' + str(result))
##    print('Absolute difference: ' + str(absdif))
##    
##    if absdif <= margin :
##        keepgoing = False
##    else :
##        if result >= desiredvalue:
##            startvalue = guess
##        else :
##            endvalue = guess
    

# Driver program to test above function
minvalue = 1
index = -1;

for n in range(892371400, 892371500) :
    result = phi(n)/(n-1)
    if result < minvalue:
        minvalue = result
        index = n

print(index)
print(minvalue)
    
    



    
     
  
# This code is contributed 
# by Nikita Tiwari. 
