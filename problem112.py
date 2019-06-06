def isBouncy(n):
    increasing = False
    decreasing = False
    s = str(n)
    for i in range(1, len(s)):
        if int(s[i-1]) < int(s[i]):
            decreasing = True
        if int(s[i-1]) > int(s[i]):
            increasing = True
        if increasing and decreasing:
            return True

    return False

count = 0
total = 100
ratio = count / total
i = 100
while ratio < 0.99:
    i = i + 1
    if isBouncy(i):
        count = count + 1
    total = total + 1
    ratio = count/total
    
        
