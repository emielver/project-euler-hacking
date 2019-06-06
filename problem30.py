def canBeWritten(n):
    s = str(n)
    return sum(int(s[x]) ** 5 for x in range(len(s))) == n 


numbers = []
for i in range(32, 295245):
    if canBeWritten(i):
        numbers.append(i)
print(sum(numbers))
