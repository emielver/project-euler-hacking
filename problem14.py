def collatz(n):
    # finished
    if n == 1:
        return 1
    # if n is even
    if n % 2 == 0:
        n = int(n/2)
        return 1 + collatz(n)
        # else
    else:
        n = int(3*n + 1)
        return 1 + collatz(n)

maxSize = 0
maxNumber = 0
for i in range(100000, 1000000):
    size = collatz(i)
    if size > maxSize:
        maxSize = size
        maxNumber = i
        print("Max size = %d, number = %d" % (maxSize, maxNumber))
print(maxNumber)


