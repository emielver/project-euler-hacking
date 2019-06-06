a = 2
b = 3
i = 2
finished = False
while i < 100:
    i += 1
    if i % 3 == 0:
        c = (int(i/3) * 2) * b + a
    else:
        c = int(a + b)
    a = b
    b = c
s = str(b)
total = 0
for char in s:
    total += int(char)
print(total)
