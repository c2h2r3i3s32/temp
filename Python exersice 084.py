def median_of_three(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
median = median_of_three(num1, num2, num3)
print(f'The median of {num1}, {num2}, and {num3} is {median}.')