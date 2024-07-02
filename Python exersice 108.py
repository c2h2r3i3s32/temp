negative_numbers = []
zeros = []
positive_numbers = []

while True:
    user_input = input("Enter an integer: ")
    if user_input == "":
        break
    try:
        number = int(user_input)
        if number < 0:
            negative_numbers.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            positive_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

sorted_numbers = negative_numbers + zeros + positive_numbers

for number in sorted_numbers:
    print(number)

