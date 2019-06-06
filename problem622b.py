upper = 60

number = 2 ** upper
file = open("candidates.txt", "r")
candidates = file.readlines()[0].split(" ")
candidates = [int(candidates[i]) for i in range(len(candidates)-1)]
file.close()
print(len(candidates))
endIndex = len(candidates)
lowerBound = candidates[-1]
upperBound = lowerBound * 10
for i in range(lowerBound, 1152921504606846976, 2):
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
file = open("candidates.txt", "a")
for i in range(endIndex, len(candidates)):
    file.append(str(candidates[i] + " "))
file.close()
