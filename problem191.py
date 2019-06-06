import time
start = time.time()
# Recursive dynamic program
def recur(days,late,absent):
    ## forfeit prize
    if absent > 2 or late > 1:
        return 0
    ## no days left and still alive then count as win
    elif days == 0:
        return 1
    ## if not finished yet
    elif (days,late,absent) in D:
        ## Try again
        return D[(days,late,absent)]
    ## one more day on time
    ot = recur(days - 1,late,0)
    ## one more day absent
    ab = recur(days - 1,late,absent + 1)
    # one more day late
    la = recur(days - 1,late + 1,0)
    # Add to dictionary
    D[(days,late,absent)] = ot + ab + la
    ## return the sum of the number of days on time, late and absent
    return ot + ab + la
# create empty dictionary
D = {}
print(recur(30,0,0))
print(str(time.time() - start) + "ms")
