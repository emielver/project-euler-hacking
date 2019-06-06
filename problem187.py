from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]


primes = findPrimes(50000000)
print("Primes found")
upper = 10**8
count = 0
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] < upper:
            count += 1
        else:
            break
    if primes[i] > upper:
        break
    if i % 500000 == 0:
        print(i)
print(count)
