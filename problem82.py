file = open("p082_pmatrix.txt", "r")
lines = file.readlines()
file.close()

dimensions = len(lines)

matrix = [[0 for x in range(dimensions)] for y in range(dimensions)]

for i in range(dimensions):
    numbers = lines[i].strip().split(",")
    for j in range(len(numbers)):
        matrix[i][j] = int(numbers[j])

dimensions -= 1
for i in range(dimensions, -1, -1):
    for j in range(dimensions, -1, -1):
        if i < dimensions and j < dimensions and i > 0:
            matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1], matrix[i-1][j])
        elif i < dimensions:
            matrix[i][j] += matrix[i+1][j]
        elif j < dimensions:
            matrix[i][j] += matrix[i][j+1]
        elif i > 0:
            matrix[i][j] += matrix[i-1][j]
print(matrix)
