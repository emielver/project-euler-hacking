from itertools import compress

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = findPrimes(7654321)
print("Found the primes")
def isPandigital(n):
    s = str(n)
    array = [0 for x in range(10)]
    for c in s:
        d = int(c)
        array[d] += 1
    if n == 2143:
        print(array)
    for i in range(1, len(s)+1):
        if not array[i]== 1:
            return False
    return True

for i in range(len(primes)-1, 0, -1):
    if isPandigital(primes[i]):
        print(primes[i])
        break
