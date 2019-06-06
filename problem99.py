import math

file = open("p099_base_exp.txt", "r")

lines = file.readlines()

highestNumber =  0
index = 0
for i in range(len(lines)):
    parts = lines[i].strip().split(",")
    base = int(parts[0])
    power = int(parts[1])

    number = (math.log(base) * power)
    if number > highestNumber:
        highestNumber = number
        index = i
file.close()
print(index + 1)
