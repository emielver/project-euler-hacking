ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["teen", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = "hundred"
thousands = "thousand"
def length(n):
    string = str(n)
    inWords = ""
    # if 1000's
    if len(string) == 4:
        # thousands
        inWords = inWords + "onethousand"
        # hundreds
        inWords = inWords + ones[int(string[1]) - 1]
        inWords = inWords + "and"
        # tens
        if not string[2] == 1:
            inWords = inWords + tens[int(string[2]) - 1]
            inWords = inWords + ones[int(string[3]) - 1]
            return inWords
        else:
            if string[3] > 5:
                inWords = inWords + ones[int(string[3]) - 1]
                inWords = inWords + tens[0]
                return inWords
            else:
                if string[3] == 1:
                    inWords = inWords + "eleven"
                elif string[3] == 2:
                    inWords = inWords + "twelve"
                elif string[3] == 3:
                    inWords = inWords + "thirteen"
                elif string[3] == 4:
                    inWords = inWords + "fourteen"
                else:
                    inWords = inWords + "fifteen"
                return inWords
    elif len(string) == 3:
        #hundreds
        inWords = inWords + ones[int(string[0]) - 1]
        inWords = inWords + "and"
        # tens
        if not string[1] == 1:
            inWords = inWords + tens[int(string[1]) - 1]
            inWords = inWords + ones[int(string[2]) - 1]
            return inWords
        else:
            if string[2] > 5:
                inWords = inWords + ones[int(string[2]) - 1]
                inWords = inWords + tens[0]
                return inWords
            else:
                if string[2] == 1:
                    inWords = inWords + "eleven"
                elif string[2] == 2:
                    inWords = inWords + "twelve"
                elif string[2] == 3:
                    inWords = inWords + "thirteen"
                elif string[2] == 4:
                    inWords = inWords + "fourteen"
                else:
                    inWords = inWords + "fifteen"
                return inWords
    elif len(string) == 2:
        # tens
        if not string[0] == 1:
            inWords = inWords + tens[int(string[0]) - 1]
            inWords = inWords + ones[int(string[0]) - 1]
            return inWords
        else:
            if string[1] > 5:
                inWords = inWords + ones[int(string[1]) - 1]
                inWords = inWords + tens[0]
                return inWords
            else:
                if string[1] == 1:
                    inWords = inWords + "eleven"
                elif string[1] == 2:
                    inWords = inWords + "twelve"
                elif string[1] == 3:
                    inWords = inWords + "thirteen"
                elif string[1] == 4:
                    inWords = inWords + "fourteen"
                else:
                    inWords = inWords + "fifteen"
                return inWords
    else:
        inWords = inWords + ones[int(string[0]) - 1]
        return inWords


upperRange = 1000
total = ""
for i in range(1, upperRange+1):
    total = total + length(i)

print(len(total))
