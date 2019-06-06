upperBound = 1000

currentSum = 0

for i in range(1, upperBound):
    if i%3 == 0:
        currentSum = currentSum + i
    elif i%5 == 0:
        currentSum = currentSum + i

print(currentSum)
