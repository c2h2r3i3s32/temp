width = int(input())
lenth = int(input())
unit = input("enter your unit")
while unit != 'feet' or 'meter':
    unit = input("enter your unit")
print(width * lenth, unit)
