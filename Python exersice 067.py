total_cost = 0.0

while True:
    people = input("Enter the age of the guest: ")
    
    if people == "":
        break
    
    try:
        age = int(people)
        
        if age <= 2:
            total_cost += 0.00
        elif 3 <= age <= 12:
            total_cost += 14.00
        elif age >= 65:
            total_cost += 18.00
        else:
            total_cost += 23.00
            
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print("Total admission cost for the group:", total_cost)
