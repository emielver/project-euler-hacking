import time

def incrementDice(dice, n):
    for i in range(n, len(dice), n):
        dice[i] += 1
    return dice

def count(dice):
    c = 0
    for i in range(1, len(dice)):
        if dice[i] %  6 == 1:
            print(i)
            c += 1
    return c

for p in range(9, 10):
    start = time.time()
    n = 10 ** p
    dice = [1 for x in range(n+1)]
    for i in range(2, n+1):
        dice = incrementDice(dice, i*i)
    print("~~~~~~%d~~~~~~" % n)
    print(count(dice))
    print(time.time() - start)
