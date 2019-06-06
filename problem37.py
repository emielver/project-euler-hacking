from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = findPrimes(10000000)

def truncatableLeft(n):
    s = str(n)
    for i in range(len(s)):
        spart = s[i:]
        if not int(spart) in primes:
            return False
    return True

def truncatableRight(n):
    s = str(n)
    for i in range(1, len(s)):
        spart = s[:-i]
        if not int(spart) in primes:
            return False
    return True


def truncatable(n):
    return truncatableLeft(n) and truncatableRight(n)
trunc = []
i = 4
while True:
    num = primes[i]
    if truncatable(num):
        trunc.append(num)
        print(trunc)
    if len(trunc) == 11:
        break
    i += 1
print(sum(trunc))
    
