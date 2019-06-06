from fractions import gcd

def lcm(numbers):
    output = numbers[0]
    for i in range(1, len(numbers)):
        number = numbers[i]
        output = output * number // gcd(output, number)
    return output

def P(s, N):
    if s == 1:
        return (N-1) // 2
    else:
        x0 = lcm([x for x in range(2, s+1)])
        x1 = lcm([x for x in range(2, s+2)])
        return (N-2) // x0 - (N-2) // x1
    
print(sum([P(i, 4**i) for i in range(1, 32)]))
    
