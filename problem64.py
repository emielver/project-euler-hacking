import time

start = time.time()
upper = 10000
total = 0
# Algorithm from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
for i in range(2, upper+1):
    r = lim = int(i ** 0.5)
    if (lim ** 2 == i): continue
    d = 1
    period = 0
    while d != 1 or period == 0:
        d = (i - r * r) // d
        r = (lim + r) // d * d - r
        period += 1
    if period % 2 == 1:
        total += 1
print(time.time() - start)
print(total)
