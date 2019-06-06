import time

start = time.time()
num=3
counter=0
# While we haven't found the 124th divisor yet
while counter<124:
    # check the next odd number
    num+=2
    i=3
    t=[1,1,1,3]
    end=0
    while end==0:
        i+=1
        t.append((t[i-1]+t[i-2]+t[i-3])%num)
        if t[i]==1 and t[i-1]==1 and t[i-2]==1:
            end=1
        elif t[i]==0:
            end=2
    # if not divisible, we found another one
    if end==1:
        counter+=1
print(time.time() - start)
print(num)
