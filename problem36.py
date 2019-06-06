def checkPalindrome(potential):
    return str(potential) == str(potential)[::-1]

def decToBin(x):
    return int(bin(x)[2:])

total = 0

for number in range(1, 1000000):
    binNumber = decToBin(number)

    if checkPalindrome(number) and checkPalindrome(binNumber):
        total = total + number
