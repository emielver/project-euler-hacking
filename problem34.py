import math

def isCurious(n):
    s = str(n)
    total = 0
    for c in s:
        num = int(c)
        total += math.factorial(num)
    return total == n


curious = []
for i in range(3, 1000000):
    if isCurious(i):
        curious.append(i)
