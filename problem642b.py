import time
import bisect

start = time.time()
# sum of primes Lucy's for PE10
def sumPrimes(n):
    root = int(n**0.5)
    S1 = [(n//x)*((n//x)+1)//2-1 if x else 0 for x in range(root+1)]
    S2 = [x*(x+1)//2-1 for x in range(root+1)]
    primes = []
    for p in range(2,root+1):
        if S2[p] == S2[p-1]: continue
        primes.append(p)
        sp = S2[p-1]
        psquared = p ** 2
        fin = min(root, n//psquared)
        for i in range(1, fin+1):
            u = p * i
            if u <= root:
                S1[i] -= p*(S1[u]-sp)
            else:
                S1[i] -= p*(S2[n//u]-sp)
        if psquared <= root:
            for i in range(root, psquared-1, -1):
                S2[i] -= p*(S2[i//p]-sp)
    return S1, primes


number = 201820182018
# brute force
S, primes = sumPrimes(number)
root = int(number ** 0.5)
result = sum(S) - root*S[root]
l = [1]
for prime in primes:
    k = bisect.bisect(l, number//prime)
    l = l[:bisect.bisect(l, number//prime)]
    newL = []
    dummyPrime = prime
    multipleCount = 0
    while dummyPrime <= number:
        multipleCount += bisect.bisect(l, number//dummyPrime)
        k = bisect.bisect(l, number//dummyPrime//(prime+1))
        newL += [dummyPrime*l[i] for i in range(k)]
        dummyPrime *= prime
    result += prime * multipleCount
    newL.sort()
    l = l[:bisect.bisect(l, number//(prime+1))]
    l += newL
    l.sort()
print(result)
print(result%10**9)
print(time.time() - start)
