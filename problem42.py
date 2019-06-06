file = open("p042_words.txt", "r")
lines = file.read()
words = lines.strip().split(",")

values = []
maxValue = 0
maxIndex = 0
for word in words:
    word = word.replace('"', "")
    value = 0
    for letter in word:
        value += (ord(letter.lower())-96)
    values.append(value)
    if value > maxValue:
        maxValue = value

triangles = []
triangle = 0
i = 0
while (triangle < maxValue):
    triangle = 0.5 * i * (i+1)
    triangles.append(triangle)
    i = i + 1

count = 0
for value in values:
    if value in triangles:
        count += 1

print(count)
