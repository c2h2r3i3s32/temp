def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1

operator = input("Enter a mathematical operator (+, -, *, /, ^): ")
result = precedence(operator)
    
if result == -1:
    print(f"The input '{operator}' is not a recognized operator.")
else:
    print(f"The precedence of the operator '{operator}' is {result}.")
