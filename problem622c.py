upper = 10

number = 2 ** upper
candidates = []

lowerBound = 2
upperBound = 1000000
for i in range(lowerBound,upperBound, 2):
    if number % (i-1) == 1:
        addTo = True
        for j in range(1, upper):
            newNumber = 2 ** j
            if newNumber % (i-1) == 1:
                addTo = False
                break
        if addTo:
            candidates.append(i)

print(len(candidates))

