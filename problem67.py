import time

start = time.time()
file = open("p067_triangle.txt", "r")
lines = file.readlines()
matrix = [[0 for x in range(len(lines))] for y in range(len(lines))]
for i in range(len(lines)):
    parts = lines[i].split(" ")
    for j in range(len(parts)):
        matrix[i][j] = int(parts[j].strip())
    for j in range(len(parts), len(lines)):
        matrix[i][j] = 0
file.close()


sumMatrix = matrix
# for every row
for i in range(1, len(matrix)):
    # for every element in i
    for j in range(0, i+1):
        sumMatrix[i][j] = matrix[i][j] + max(sumMatrix[i-1][j], sumMatrix[i-1][j-1])
finish = time.time()
print(max(sumMatrix[-1]))
print("Runtime: %d ms" % (start - finish))
