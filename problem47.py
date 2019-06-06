def primeFactors(n):
        i = 2
        factors = []
        count = 0                           #added to test optimization
        while i * i <= n:
            count += 1                      #added to test optimization
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

def distinctFactors(factors):
    distinct = []
    for factor in factors:
        if factor not in distinct:
            distinct.append(factor)
    return len(distinct)

consec = 4
num = 10
finished = False

while not finished:
    num += 1
    factors = [[] for x in range(consec)]
    finished = True
    for j in range(consec):
        factors[j] = primeFactors(num+j)
        if len(factors[j]) < consec:
            finished = False
    # count distinct prime factors used in case
    if finished:
        for i in range(len(factors)):
            if distinctFactors(factors[i]) < consec:
                finished = False
            
print(num)
for i in range(consec):
    print(primeFactors(num + i))
