def checkPalindrome(potential):
    return str(potential) == str(potential)[::-1]

candidate = 0
candidates = [[0 for x in range(3)] for y in range(1000000)]
index = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if checkPalindrome(product):
            if product > candidate:
                candidate = product
            candidates[index][0] = product
            candidates[index][1] = i
            candidates[index][2] = j
            index = index + 1

print(candidate)
print("Product = %d, made by %d * %d" % (candidates[index-1][0], candidates[index-1][1], candidates[index-1][2]))
