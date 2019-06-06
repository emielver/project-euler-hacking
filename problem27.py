from itertools import compress

def rwh_primes1v2(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def isPrime(test):
    i = 0
    while primes[i] <= test:
        if primes[i] == test:
            return True
        i = i + 1
    return False


primes = rwh_primes1v2(100000)
print("Primes found!")

maxA = 0
maxB = 0
maxN = 0

for a in range(-999, 1000, 2):
    for b in range(168):
        n = 0
        while (isPrime(abs( n * n + a * n + primes[b]))):
            n = n + 1
        if n > maxN:
            maxA = a
            maxB = primes[b]
            maxN = n

print("%d and %d yields %d primes" % (maxA, maxB, maxN))

