import math

a = 0
b = 0
c = 0
for i in range(1,500):
    a = i * i
    for j in range(1, 500):
        b = j * j

        c = a + b

        if (math.sqrt(a) + math.sqrt(b) + math.sqrt(c) == 1000):
            print(math.sqrt(a) * math.sqrt(b) * math.sqrt(c))
