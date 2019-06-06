import math

def combo(n, r):
    num = math.factorial(n)
    denom = math.factorial(r) * (math.factorial(n-r))
    return int(num/denom)


count = 0
for i in range(23, 101):
    for j in range(0, i+1):
        if combo(i, j) > 1000000:
            count += 1
