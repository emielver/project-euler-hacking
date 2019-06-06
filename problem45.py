def isPentagonal(n):
    answer = (((1+ 24 * n) ** 0.5) + 1 )/ 6
    return answer == int(answer)

def isTriangular(n):
    answer = (((8*n + 1) ** 0.5) - 1)/2
    return answer == int(answer)

finished = False
i = 143
while not finished:
    i += 1
    number = i * (2 * i - 1)

    if isPentagonal(number) and isTriangular(number):
        print(number)
        finished = True
