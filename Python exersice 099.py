def to_base_10(number, base):
    try:
        return int(number, base)
    except ValueError:
        return None

def from_base_10(number, base):
    if number == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

def main():
    try:
        input_base = int(input("Enter the input base (2-16): "))
        output_base = int(input("Enter the output base (2-16): "))
        number = input("Enter the number: ").upper()

        if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
            print("Error: Bases must be between 2 and 16.")
            return
        
        base_10_number = to_base_10(number, input_base)
        if base_10_number is None:
            print("Error: Invalid number for the given input base.")
            return
        
        converted_number = from_base_10(base_10_number, output_base)
        print(f"The number {number} in base {input_base} is {converted_number} in base {output_base}.")

    except ValueError:
        print("Error: Invalid input. Please enter valid integers for the bases and a valid number.")

main()

