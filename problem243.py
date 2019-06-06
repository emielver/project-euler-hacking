from itertools import compress

# Find primes

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

# Euclidean Algorithm
def gcd(a, b):
    while not b == 0:
        t = b
        b = a % b
        a = t
    return a

def resilience(denom):
    res = 0
    for i in range(1, denom+1):
        divisor = gcd(i,denom)
        # print("GCD %d between %d and %d" % (divisor, i, denom))
        # if we don't get a whole number aka can't simplify
        if  divisor == 1 :
            res += 1
    return res
primes = findPrimes(100000)
print("Primes found")
frac = (15499/94744)
for i in range(12, 200000000):
    if i not in primes:
        res = resilience(i)
        if res / (i-1) < frac:
            break
    if i % 10000 == 0:
        print(i)
        # print("Resilience of %d is %d / %d or %f" % (i, res, i-1, res/(i-1)))

