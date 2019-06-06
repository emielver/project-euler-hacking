## source: https://www.alpertron.com.ar/QUAD.HTM

b = 15
n = 21
lowerBound = 1000000000000

while n < lowerBound:
    tempB = 3*b + 2*n - 2
    tempN = 4*b + 3*n - 3

    b = tempB
    n = tempN
print(b)
