width = int(input('enter width'))
lenth = int(input('enter lenth'))
unit = input('enter unit')
r = False

while r == False:
    if unit != 'feet':
        if unit != 'meter':
            unit = input('enter unit')

    else:
        r =True

print(width * lenth, unit)
