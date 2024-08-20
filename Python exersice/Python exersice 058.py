year = int(input("Enter the year: ")) 
month = int(input("Enter the month: ")) 
day = int(input("Enter the day: ")) + 1
year4 = year % 4
if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if day >= 32:
        day = day - 1
        month = month + 1
if month == 4 or 6 or 9 or 11:
    if day >= 31:
        day = day - 1
        month = month + 1

if month == 2:
    if  year4 == 4:
        if day >= 29:
            day = day - 1
            month = month + 1
    else:
        if day >= 30:
            day = day - 1
            month = month + 1

if month >= 12:
    year = year + 1
    month = 1

date = (year, month, day)
print(date)
