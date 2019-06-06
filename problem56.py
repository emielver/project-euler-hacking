def digitSum(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    return total


maxDigSum = 0
for i in range(2, 100):
    for j in range(1, 100):
        digSum = digitSum(i ** j)
        if digSum > maxDigSum:
            maxDigSum = digSum
print(maxDigSum)
