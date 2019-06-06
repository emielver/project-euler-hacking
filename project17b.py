ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["teen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = "hundred"
thousands = "thousand"
def length(n):
    inWords = ""
    string = str(n)
    if len(string) == 2:
        tenColumn = int(string[0])
        oneColumn = int(string[1])
        if tenColumn == 1:
            if oneColumn == 0:
                inWords = "ten"
            elif oneColumn == 1:
                inWords = "eleven"
            elif oneColumn == 2:
                inWords = "twelve"
            elif oneColumn == 3:
                inWords = "thirteen"
            elif oneColumn == 4:
                inWords = "fourteen"
            elif oneColumn == 5:
                inWords = "fifteen"
            elif oneColumn == 8:
                inWords = "eighteen"
            else:
                inWords = ones[oneColumn - 1] + tens[tenColumn - 1]
        else:
            if oneColumn == 0:
                inWords = tens[tenColumn - 1]
            else:
                inWords = tens[tenColumn - 1] + ones[oneColumn - 1]
    else:
        oneColumn = int(string[0])
        inWords = ones[oneColumn - 1]
    return inWords
    


upperRange = 99
numbers = []
total = 0
for i in range(1, upperRange+1):
    word = length(i)
    numbers.append(word)
    total = total + len(word)
    
for i in range(1, 10):
    hundred = ones[i-1] + hundreds
    total = total + len(hundred)
    # print(hundred)
    # x hundred and
    for number in numbers:
        word = ones[i-1] + hundreds + "and" + number
        total = total + len(word)
        # print(word)
thousand = "onethousand"
total = total + len(thousand)
print(total)
