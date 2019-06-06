coins = [1, 2, 5, 10, 20, 50, 100, 200]
def combo(amount, currentCoin):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    numberCombos = 0
    for i in range(currentCoin, len(coins)):
        numberCombos += combo(amount - coins[i], i)
    return numberCombos
for i in range(len(coins)):
    print("Value = %d can be represented in %d ways" % (coins[i], combo(coins[i],0)))
