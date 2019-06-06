from itertools import compress
import time

def findPrimes(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def compute():
	LIMIT = 10**9
	primes = findPrimes(100)
	
	def count(primeindex, product):
		if primeindex == len(primes):
			return 1 if product <= LIMIT else 0
		else:
			result = 0
			while product <= LIMIT:
				result += count(primeindex + 1, product)
				product *= primes[primeindex]
			return result
	
	return str(count(0, 1))
start = time.time()
result = compute()
print(result)
end = time.time()
print("Running time is %ss" % (end - start))
