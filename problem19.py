def isLeapYear(n):
    # if divisible by 400 for sure leap year
    if n % 400 == 0:
        return True
    # otherwise if not on a century
    elif not n % 100 == 0:
        # if divisible by 4 true, otherwise false
        return (n%4==0)
    # otherwise false
    return False

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sundayCount = 0
dayIndex = 1
for year in range(1901,2001):
    leap = False
    if year%4 == 0:
        leap = isLeapYear(year)
    for i in range(len(months)):
        if i == 1 and leap:
            print("%d is a leap year!" % year)
            dayIndex = dayIndex + 29%7
        else:
            dayIndex = dayIndex + (months[i] % 7)
        dayIndex = dayIndex % 7

        if dayIndex == 6:
            sundayCount = sundayCount + 1


