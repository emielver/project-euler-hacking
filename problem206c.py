def match(n):
    string = str(n)
    isMatch = False
    return all(int(s[x*2]) == x+1 for x in range(9))

n = 138902663    
while not match(n**2):
    n -= 2

print ("Project Euler 206 Solution =", n*10)   
