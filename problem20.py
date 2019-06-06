product = 1

for i in range(1,100):
    if i % 10 == 0:
        i = int(i / 10)
    product = product * i

productList = str(product)
total = 0
for digit in productList:
    digit = int(digit)
    total = total + digit
print(total)
