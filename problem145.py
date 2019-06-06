def reverse(n):
    s = str(n)
    return s[::-1]

def isReversible(n):
    rev = int(reverse(n))
    if len(str(rev)) == len(str(n)):
        tot = rev + n
        s = str(tot)
        for c in s:
            if (int(c) % 2 == 0):
                return False
        return True
    return False

upper = 10**9
count = 0
for i in range(1, int(upper/2)):
    if isReversible(i):
        count += 1

print(count*2)
