s = "0."
i = 1
while (len(s) < 1000002):
    s += str(i)
    i += 1


prod = int(s[2]) * int(s[11]) * int(s[101]) * int(s[1001]) * int(s[10001]) * int(s[100001])* int(s[1000001])
print(prod)
