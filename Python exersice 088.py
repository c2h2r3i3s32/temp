def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = float(input("Enter the first length: "))
b = float(input("Enter the second length: "))
c = float(input("Enter the third length: "))
    
if triangle(a, b, c):
    print(f"The lengths {a}, {b}, and {c} can form a triangle.")
else:
    print(f"The lengths {a}, {b}, and {c} cannot form a triangle.")
