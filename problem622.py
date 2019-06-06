def getDeck(n):
    deck = [0 for x in range(n)]
    for i in range(1,n+1):
        deck[i-1] = i
    return deck

def shuffleDeck(deck):
    shuffledDeck = [0 for x in range(len(deck))]
    half = int(len(deck)/2)
    counter = 0
    for i in range(0, half):
        shuffledDeck[counter] = deck[i]
        counter = counter + 1
        shuffledDeck[counter] = deck[half + i]
        counter = counter + 1
    return shuffledDeck

def isDeck(deck1, deck2):
    for i in range(len(deck1)):
        if not deck1[i] == deck2[i]:
            return False
    return True

deckSizes = []
for i in range(2,1000, 2):
    originalDeck = getDeck(i)
    shuffDeck = shuffleDeck(originalDeck)
    count = 1

    while not (isDeck(shuffDeck, originalDeck)):
        shuffDeck = shuffleDeck(shuffDeck)
        count = count + 1
    if count == 6:
        deckSizes.append(i)

print(deckSizes)
