def isPandigital(s):
    array = [0 for x in range(10)]
    for c in s:
        d = int(c)
        array[d] += 1
    for i in range(1, 10):
        if not array[0] == 0:
             return False
        elif not array[i]== 1:
            return False
    return True


for i in range(99999, 0, -1):
    s = str(i * 1) + str(i*2)
    multiple = 3
    while len(s) < 9:
        s += str(i * multiple)
        multiple += 1
    if isPandigital(s):
        print(s)
        break
