import re

file = open("p089_roman.txt", "r")
originalNumerals = file.read()
oldLength = len(originalNumerals)
newNumerals = re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", "ev", originalNumerals)
newLength = len(newNumerals)

print(oldLength - newLength)
