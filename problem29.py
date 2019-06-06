numbers = []
for a in range(2, 101):
    for b in range(2, 101):
        power = a ** b
        if power not in numbers:
            numbers.append(power)
print(len(numbers))
