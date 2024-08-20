number = [3, 4, 5, 6, 7, 8, 9, 10]
name = [0, 1, 2, "Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]
side = int(input("The number of the side"))
if side in (number):
    shape = name[side]
    print(shape)
else:
    print("Please enter number 3 to 10")