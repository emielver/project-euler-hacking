w

def specialProperty(n):
    s = str(n)
    numb = int(s[1:4])
    if numb % 2 == 0:
        numb = int(s[2:5])
        if numb % 3 == 0:
            numb = int(s[3:6])
            if numb % 5 == 0:
                numb = int(s[4:7])
                if numb % 7 == 0:
                    numb = int(s[5:8])
                    if numb % 11 == 0:
                        numb = int(s[6:9])
                        if numb % 13 == 0:
                            numb = int(s[7:10])
                            if numb % 17 == 0:
                                return True
    return False

def check(n):
    if isPandigital(n):
         return specialProperty(n)
           
    return False

special = []
for i in range(1234567884, 987654322, 17):
    if check(i):
        special.append(i)
print(sum(special))
