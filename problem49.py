from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def containDigits(n1, n2, n3):
    s1 = str(n1)
    s2 = str(n2)
    s3 = str(n3)
    contains = True
    for c in s1:
        if not c in s2 or not c in s3:
            contains = False
    for c in s2:
        if not c in s3 or not c in s1:
            contains = False
    for c in s3:
        if not c in s1 or not c in s2:
            contains = False
    return contains
    

primes = findPrimes(10000)
finished = False
while not finished:
    for i in range(168, len(primes)):
        currPrime = primes[i]
        for j in range(i+1, len(primes)):
            nextPrime = primes[j]
            diff = nextPrime - currPrime
            thirdPrime = nextPrime + diff
            if thirdPrime in primes and containDigits(currPrime, nextPrime, thirdPrime):
                print("First prime = %d, second prime = %d, third prime = %d with a diff of %d" % (currPrime, nextPrime, thirdPrime, diff))
                finished = True
                break
                
