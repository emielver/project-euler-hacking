def isPandigital(n):
    s = str(n)
    array = [0 for x in range(10)]
    for c in s:
        d = int(c)
        array[d] += 1
    for i in range(1, 10):
        if not array[0] == 0:
             return False
        elif not array[i]== 1:
            return False
    return True


products = []
for a in range(1, 10000):
    for b in range(a, 10000):
        product  = a * b
        s = str(product) + str(a) + str(b)
        if len(s) > 10:
            break
        if isPandigital(int(s)):
            if product not in products:
                products.append(product)
print(sum(products))
