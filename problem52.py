def digits(n):
    s = str(n)
    digs = []
    for c in s:
        if c not in digs:
            digs.append(c)
    return digs

i = 0
finished = False
while not finished:
    i += 1
    oldDigits = sorted(digits(i))
    finished = True
    for j in range(2, 7):
        num = i * j
        newDigits = sorted(digits(num))

        if not newDigits == oldDigits:
            finished = False
            break
        else:
            oldDigits = newDigits
        
print(i)
