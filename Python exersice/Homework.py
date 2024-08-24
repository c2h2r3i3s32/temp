def parse_input(user_input):
    parts = user_input.split()
    
    if len(parts) != 3:
        raise ValueError("Input does not consist of three elements.")
    
    num1, operator, num2 = parts
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("The first and third elements must be numbers.")
    
    if operator not in ('+', '-'):
        raise ValueError("The operator must be '+' or '-'.")
    
    return num1, operator, num2

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

while True:
    user_input = input("Enter a formula (or type 'quit' to exit): ")
        
    if user_input == 'quit':
        break

    num1, operator, num2 = parse_input(user_input)
    result = calculate(num1, operator, num2)
    print(f"Result: {result}")


