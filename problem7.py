import math

def primeFinder(count):
    actualNumber = 3
    primes = [2]
    while len(primes) != count:
        number = actualNumber
        isPrime = True
        for divisor in primes:
            while number % divisor == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)
        actualNumber = actualNumber + 2
    return primes


primes = primeFinder(10001)
print(primes[-1])

