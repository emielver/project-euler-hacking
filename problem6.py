

def sumOfSquares(n):
    squareSum = 0

    for i in range(1, n+1):
        squareSum = squareSum + (i * i)

    return squareSum

def squareOfSum(n):
    sumSquare = 0

    for i in range(1, n+1):
        sumSquare = sumSquare + i

    sumSquare = (sumSquare * sumSquare)
    return sumSquare

squareSum = sumOfSquares(100)
sumSquare = squareOfSum(100)

diff = sumSquare - squareSum
        
