numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

average = sum(numbers) / len(numbers)
    
below_average = [num for num in numbers if num < average]
average_values = [num for num in numbers if num == average]
above_average = [num for num in numbers if num > average]

print(f"\nAverage: {average}\n")
    
print("Below average values:")
for num in below_average:
    print(num)
    
if average_values:
    print("\nAverage values:")
    for num in average_values:
        print(num)
    
print("\nAbove average values:")
for num in above_average:
    print(num)

