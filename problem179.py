upper = 10 ** 7
half = upper // 2
counts = [0 for x in range(upper + 1)]

# base number
for i in range(2, half):
    for j in range(i * 2, upper, i):
        counts[j] += 1

print("Finished!")
total = 0      
for i in range(2, len(counts)-1):
    if counts[i] == counts[i+1]:
        total += 1
print(total)
