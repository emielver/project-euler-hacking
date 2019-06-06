def isPalindrome(potential):
    return str(potential) == str(potential)[::-1]

def getReverse(n):
    s = str(n)
    return int(s[::-1])

def mainThing(n, count):
    if count > 50:
        return count
    rev = getReverse(n)
    total = rev + n
    if isPalindrome(total):
        return count
    else:
        count += 1
        return mainThing(total, count)
count = 0
for i in range(1, 10000):
    counts = mainThing(i, 1)
    if counts == 51:
        count += 1
print(count)
