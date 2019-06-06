def isCorrect(n):
    string = str(n)
    for i in range(9):
        if not int(string[i*2]) == i+1:
            return False
    return True

n = 138902663    
while not isCorrect(n**2):
    n -= 2

n = n * 10
print(n)   
