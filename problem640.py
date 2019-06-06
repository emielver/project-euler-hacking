import random

numberSimulations = 100000000
numberCards = 12

def diceRoll():
    return random.randint(1,6)


def game():
    array = [0 for x in range(numberCards)]
    arrayDone = False
    turnCounter = 0 
    while not arrayDone:
        turned = False
        roll1 = diceRoll()
        roll2 = diceRoll()
        maximum = max(roll1, roll2)
        minimum = min(roll1, roll2)
        total = roll1 + roll2
        # if total above 6, take it
        if total > 6:
            # if unturned
            if array[total-1] == 0:
                # turn it
                array[total-1] = 1
                # record that you turned it
                turned = True
        # if you haven't turned one yet
        if not turned:
            # if you can pick the lowest number
            if array[minimum-1] == 0:
                # turn it
                array[minimum-1]  = 1
            # else pick highest single that you can (still lower than sum so better)
            elif array[maximum-1] == 0:
                # turn it
                array[maximum-1] = 1
            # else flip the sum (since highest chance if sum less than 6)
            else:
                # if total less than 6
                if total < 6:
                    if array[total-1] == 0:
                        # turn it
                        array[total-1] = 1
                    # otherwise
                    else:
                        # turn it back
                        array[total-1] = 0
                # otherwise turn back max
                else:
                    array[maximum-1] = 0
        arrayDone = True
        for elem in array:
            if elem == 0:
                arrayDone = False
##        print("Round %d, rolls = %d %d" % (turnCounter, roll1, roll2))
##        print(array)
        turnCounter = turnCounter + 1
    return turnCounter

turns = []
for i in range(numberSimulations):
    turns.append(game())

print(str(sum(turns)/numberSimulations))

