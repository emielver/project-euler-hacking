from math import factorial

n = 15
a = [[0 for x in range(16)] for x in range(16)]

a[1][0] = 1
a[1][1] = 1

for i in range(2, n+1):
    a[i][0] = 1
    a[i][i] = factorial(i)

for x in range(2, n+1):
    for z in range(1, x):
        a[x][z] = a[x-1][z-1] * x
        a[x][z] = a[x][z] + a[x-1][z]

total = 0
for j in range(0, 8):
    total += a[n][j]

print(total)
denom = factorial(n+1)
outcome = denom/total
print(outcome)
