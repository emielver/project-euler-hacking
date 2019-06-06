cancelling = []
# denominator
for denom in range(10,99):
    for numer in range(10, denom):
        if not numer % 10 == 0 and not denom % 10 == 0:
            sNumer = str(numer)
            sDenom = str(denom)
            for c in sNumer:
                if c in sDenom:
                    actual = numer/denom
                    dumbNumer = int(sNumer.replace(c, "", 1))
                    dumbDenom = int(sDenom.replace(c, "", 1))
                    dumb = dumbNumer/dumbDenom
                    if dumb == actual:
                        cancelling.append(actual)
