power = 0
oldCount = 0
count = 0
finished = False
while not finished:
    power += 1
    base = 0
    product = 0
    oldCount = count
    while len(str(product)) <= power:
        base += 1
        product = base ** power
        if len(str(product)) == power:
            ## print("%d to the power %d is length %d" % (base, power, product))
            count += 1
    finished = oldCount == count
print(count)
