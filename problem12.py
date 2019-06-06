numberDivisors = 500


def triangleNumber(n):
    triangle = 0
    for i in range(1,n+1):
        triangle = triangle + i
    return triangle

def divisors(n):
    hcf = n
    divisors = [1, n]
    i = 2
    while i < hcf:
        if n % i == 0:
            factor = int(n / i)
            divisors.append(i)
            divisors.append(factor)
            hcf = factor
        i = i + 1
    return divisors

allDivisors = []
i = 0
triangle = 0
while len(allDivisors) < numberDivisors:
    i = i + 1
    triangle = triangleNumber(i)
    allDivisors = divisors(triangle)

print(i)
print(triangle)
