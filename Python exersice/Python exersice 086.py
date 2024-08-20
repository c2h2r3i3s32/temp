def get_ordinal(day):
    if day == 1:
        return "first"
    elif day == 2:
        return "second"
    elif day == 3:
        return "third"
    elif day == 4:
        return "fourth"
    elif day == 5:
        return "fifth"
    elif day == 6:
        return "sixth"
    elif day == 7:
        return "seventh"
    elif day == 8:
        return "eighth"
    elif day == 9:
        return "ninth"
    elif day == 10:
        return "tenth"
    elif day == 11:
        return "eleventh"
    elif day == 12:
        return "twelfth"
    else:
        return str(day)

def sing_verse(day):
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    print(f"On the {get_ordinal(day)} day of Christmas")
    print("my true love sent to me:")

    for i in range(day - 1, 0, -1):
        print(gifts[i])

    if day > 1:
        print("And " + gifts[0].lower())
    else:
        print(gifts[0])

for day in range(1, 12 + 1):
    sing_verse(day)
    print()  