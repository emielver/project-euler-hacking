def sumProperDivisors(n):
    divisors = [1]
    maxDivisor = n
    number = 2
    while (number < maxDivisor):
        if n % number == 0:
            divisors.append(number)
            divisors.append(int(n/number))
            maxDivisor = n/number
        number = number + 1
    divisors.sort()
    return(sum(divisors))

amicableNumbers = []

for i in range(1,10000):
    # d(a) = b
    sumDivisors = sumProperDivisors(i)
    # if a != b
    if not sumDivisors == i:
        # d(b) = ?
        sumOtherDivisors = sumProperDivisors(sumDivisors)
        # if d(b) = a
        if sumOtherDivisors == i:
            if i not in amicableNumbers:
                amicableNumbers.append(i)
            if sumOtherDivisors not in amicableNumbers:
                amicableNumbers.append(sumOtherDivisors)

print(amicableNumbers)  
