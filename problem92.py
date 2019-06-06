def chain(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c) ** 2
    if endEn[total] or total == 89:
        endEn[total] = True
        return 89
    if total == 1:
        return 1
    return(chain(total))
count = 0
endEn = [False for x in range(0,568)]
for i in range(2, 10000000):
    if i % 100000 == 0:
        print(i)
    if chain(i) == 89:
        count += 1
print(count)
