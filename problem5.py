factors = [11, 13, 14, 16, 17, 18, 19, 20]

for candidate in range(2520, 999999999999, 2520):
    works = False
    for factor in factors:
        if candidate % factor == 0:
            works = True
        else:
            works = False
            break
    if works:
        print(candidate)
        break
    candidate = candidate + 1
