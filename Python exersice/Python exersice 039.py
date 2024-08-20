s = int(input("Enter the volume"))
if s <= 40:
    print("quiet room")
if s > 40 and s <= 70:
    print("alarm clock")
if s > 70 and s <= 106:
    print("quiet room")
if s > 106 and s <= 130:
    print("Jackhammer")
if s > 130:
    print("out of range")