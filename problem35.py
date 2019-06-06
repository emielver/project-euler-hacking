from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = findPrimes(1000000)

circularPrimes = []
for prime in primes:
    s = str(prime)
    circular = True
    # for every starting index
    for i in range(len(s)):
        num = ""
        # for full rotation
        for j in range(len(s)):
            num += (s[(i+j) % len(s)])
        num = int(num)
        if not num in primes:
            circular = False
            break
    if circular:
        circularPrimes.append(prime)
print(len(circularPrimes))
