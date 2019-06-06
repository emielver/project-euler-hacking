upperBound = 4000000

prior1 = 1
prior2 = 0
current = 1
evenSum = 0
while current < upperBound:
    if current % 2 == 0:
        evenSum = evenSum + current

    current = prior1 + prior2
    prior2 = prior1
    prior1 = current

print("Sum is = %d" % evenSum)
