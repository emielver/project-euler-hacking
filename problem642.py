from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def highestPrimeDivisor(n, primes, top):
    if top:
        for i in range(len(primes)-1, -1, -1):
            if n % primes[i] == 0:
                return primes[i]
    else:
        highest = 0
        for prime in primes:
            if prime > n**0.5:
                return highest
            if n % prime == 0:
                highest = prime
    return 0

upper = 201820182018
primes = findPrimes(int(upper ** 0.5))
print("Primes found")
print(len(primes))
half = primes[int(len(primes)/2)]
total = 0
for i in range(2, upper+1):
    if i < half:
        total += highestPrimeDivisor(i, primes, False)
    else:
        total += highestPrimeDivisor(i, primes, True)
    if i % 100000 == 0:
        print(i)
print(total)
