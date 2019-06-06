diag = 1
for i in range(3, 1002, 2):
    power = i ** 2
    for j in range(4):
        diag += (power - (i-1)*j)
print(diag)
