import math
from itertools import compress
import time

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]


def hamming(i, j):
    if j == 0:
        return int(math.log(i)/math.log(2)) + 1
    if i == 0:
        return 0
    return hamming(i,j-1) + hamming(i/primes[j], j)

i = 0
j = 0
primes = findPrimes(100)
print("Primes found")
print(len(primes))
start = time.time()
print(hamming(10**9, len(primes)-1))
end = time.time()
print("Running time is %ss" % (end - start))
