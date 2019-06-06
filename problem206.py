for i in range(1010160030, 10000000000, 300):
    power = str(i ** 2)
    print("Number: %d, power: %s" % (i, power))
    if (power[0] == 1 and power[2] == 2
        and power[4] == 3 and power[6] == 4
        and power[8] == 5 and power[10] == 6
        and power[12] == 7 and power[14] == 8
        and power[16] == 9 and power[18] == 0):
        print(i)
