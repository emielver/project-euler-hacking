def isPandigital(s):
    array = [0 for x in range(10)]
    for c in s:
        d = int(c)
        array[d] += 1
    for i in range(0, 10):
        if not array[i]== 1:
            return False
    return True

def merge(list1, list2):
    dummyNumbs = []
    for i in range(len(list1)):
        lastDigitsThirt = list1[i][1:]
        for j in range(len(list2)):
            firstDigitsST = list2[j][:2]
            if lastDigitsThirt == firstDigitsST:
                dummyNumbs.append(list1[i] + list2[j][2:])

    return dummyNumbs
def getMultiples(numb):
    numbers = []
    for i in range(0, 1000, numb):
        s = str(i)
        if len(s) < 3:
            if len(s) > 1:
                new = "0" + s
                numbers.append(new)
        else:
            numbers.append(s)
    return numbers

numbsSevenT = getMultiples(17)
numbsThirt = getMultiples(13)
dummyNumbs = merge(numbsThirt, numbsSevenT)

numbs = getMultiples(11)
dummyNumbs = merge(numbs, dummyNumbs)

numbs = getMultiples(7)
dummyNumbs = merge(numbs, dummyNumbs)

numbs = getMultiples(5)
dummyNumbs = merge(numbs, dummyNumbs)

numbs = getMultiples(3)
dummyNumbs = merge(numbs, dummyNumbs)

numbs = getMultiples(2)
dummyNumbs = merge(numbs, dummyNumbs)

actualNumbs = []
print(len(dummyNumbs))
for i in range(1,10):
    for j in range(len(dummyNumbs)):
        actualNumbs.append(str(i) + dummyNumbs[j])
        
special = []
for string in actualNumbs:
    if isPandigital(string):
        special.append(int(string))
print(sum(special))
