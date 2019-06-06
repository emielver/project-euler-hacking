import time

start = time.time()
print(hex(16**16 - 15**16 - 15**16 - sum(map(lambda n:15**n,range(1,17))) + 14**16 + 2*sum(map(lambda n:14**n,range(1,17))) - sum(map(lambda n:13**n,range(1,17)))).upper()[2:])
print("Running time is %ss" % (time.time() - start))
