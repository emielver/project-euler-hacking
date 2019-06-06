def getTotalSum(number, power):
    return getRemainder((number-1) ** power + (number+1) ** power, number)


def getRemainder(product, divisor):
    return (product % (divisor ** 2))

totalSum = 0
for a in range(3, 1001):
    maxRemainder = 0
    for i in range(1, a**2):
        remainder = getTotalSum(a, i)
        if remainder > maxRemainder:
            maxRemainder = remainder
        if a % 2 == 0:
            if remainder == a**2 - 2*a:
                break
        else :
            if remainder == a**2 - a:
                break
    totalSum = totalSum + maxRemainder
    if (a%100 == 0):
        print(a)
print(totalSum)
