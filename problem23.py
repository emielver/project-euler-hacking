import time
 
start = time.time()

def sumOfDivisors(n):
    total = 1
    p = 2
    while p*p <= n and n > 1:
        if n%p == 0:
            j = p*p
            n = n/p
            while n % p == 0:
                j = j*p
                n = n/p
            total *= (j-1)
            total /= (p-1)
        if p == 2:
            p = 3
        else:
            p += 2
    if n > 1:
        total *= (n+1)
    return total

def sumOfProperDivisors(n):
    return int(sumOfDivisors(n) - n)

abundant = []
for i in range(1, 28123):
    if sumOfProperDivisors(i) > i:
        abundant.append(i)
numbers = [x for x in range(28123)]
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] < 28123:
            numbers[abundant[i] + abundant[j]] = 0
        else:
            break
print(sum(numbers))
