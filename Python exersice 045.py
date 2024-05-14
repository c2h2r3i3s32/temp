colour = input("Enter the position")
number = colour[1]
number = int(number)
if ( number % 2) == 0:
    if colour[0] == 'a' or colour[0] == 'c' or colour[0] == 'e' or colour[0] == 'g':
        print("white")
    if colour[0] == 'b' or colour[0] == 'd' or colour[0] == 'f' or colour[0] == 'h':
        print("black")
else:
    if colour[0] == 'a' or colour[0] == 'c' or colour[0] == 'e' or colour[0] == 'g':
        print("black")
    if colour[0] == 'b' or colour[0] == 'd' or colour[0] == 'f' or colour[0] == 'h':
        print("white")
   