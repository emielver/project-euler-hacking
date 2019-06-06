file = open("p022_names.txt", "r")

names = []
for line in file.readlines():
    for name in line.split(","):
        name = name.replace('"', "")
        name = name.lower()
        names.append(name)

names.sort()
totalValue = 0
for i in range(len(names)):
    name = names[i]
    value = 0
    for letter in name:
        value = value + (ord(letter)-96)
    totalValue = totalValue + (i+1) * value
        
print(totalValue)
