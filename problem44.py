def isPentagonal(n):
    answer = (((1+ 24 * n) ** 0.5) + 1 )/ 6
    return answer == int(answer)

finished = False
i = 1
while not finished:
    i += 1
    number1 = 0.5 * i * (3*i-1)
    for j in range(i-1, 0, -1):
        number2 = 0.5 * j * (3*j-1)

        if (isPentagonal(number1 - number2) and isPentagonal(number1 + number2)):
            print(number1 - number2)
            finished = True
