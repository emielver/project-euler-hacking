from itertools import compress
import time

upperBound = 1000000

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

start = time.time()
primes = findPrimes(upperBound)
    
total = 0
highestTotal = 0
maxTerms = 0 
numberTerms = 0
startIndex = 0
terms = []
for i in range(0, len(primes)):
    numberTerms = 1
    prime = primes[i]
    total = prime
    if len(primes) - i < maxTerms:
        break
    for j in range(i+1, len(primes)):
        total = total + primes[j]
        if total > primes[-1]:
            break
        numberTerms = numberTerms + 1
        if total in primes:
            if numberTerms > maxTerms:
                maxTerms = numberTerms
                startIndex = i
                highestTotal = total
                terms = primes[i:j+1]
end = time.time()
print("The longest sum of consecutive primes below %d that adds to a prime, contains %d terms, starts at %d, and is equal to %d."
      % (upperBound, maxTerms, primes[startIndex], highestTotal))
print(end-start)
