import math

number = 600851475143

def primeFactorFinder(number):
    primes = []
    divis2 = False
    while number % 2 == 0:
        if not divis2:
            primes.append(2)
            divis2 = True
        number = number/2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            primes.append(i)
            number = number / i

    return primes


factors = primeFactorFinder(number)
print(factors[-1])
