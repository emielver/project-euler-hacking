from random import shuffle

def game(numTurns):
    numbRed = 0
    numbBlue = 0

    sack = ['b', 'r']

    for i in range(numTurns):
        shuffle(sack)
        ball = sack[0]
        if ball == 'b':
            numbBlue += 1
        else:
            numbRed += 1
        sack.append('r')
    if numbRed < numbBlue:
        return 1
    else:
        return 0

wins = 0
sims = 100000

for i in range(sims):
    wins += game(15)

ratio = wins/sims
i = 0
while ratio < 1:
    i += 1
    ratio += (wins/sims)
print(i)
print(ratio)
print(wins/sims)
