from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = findPrimes(100000)

def twiceSquared(n):
    root = (n/2) ** 0.5
    return root == int(root)
i = 33
finished = False
while not finished:
    finished = True
    i += 2
    if i not in primes:
        for j in range(len(primes)):
            if primes[j] < i:
                diff = i - primes[j]
                if twiceSquared(diff):
                    finished = False
            else:
                break
    else:
        finished = False

