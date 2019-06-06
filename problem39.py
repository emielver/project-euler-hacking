sqra = [x ** 2 for x in range(500)]
sqrb = [x ** 2 for x in range(500)]

p = [0 for x in range(1001)]
for a in range(500):
    for b in range(500):
        c = (sqra[a] + sqrb[b]) ** 0.5
        if (int(c) == c):
            perimeter = a + b + int(c)
            if perimeter < 1000:
                p[perimeter] += 1
maxIndex = 0
maxCount = 0
for i in range(len(p)):
    if p[i] > maxCount:
        maxCount = p[i]
        maxIndex = i
print(maxIndex)
    
