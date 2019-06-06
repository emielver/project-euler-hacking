from decimal import Decimal, getcontext

getcontext().prec = 10000

upperBound = 1000
denom = 7
length = 6

for denominator in range(1, upperBound, 2):
    division = Decimal(1) / Decimal(denominator)
    s = str(division)[2:]

    for i in range(1, len(s)-(length+1)):
        if s[-i-2:-2] == s[-i-i-2:-i-2]:
            if i > length:
                length = i
                denom = denominator
            break
print(denom)
