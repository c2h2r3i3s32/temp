total_cost = 0.0
while True:
    price = input("Enter the price of the item: ")
    if price == "":
        break

    try:
        price = float(price)
        total_cost += price
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    

print("Total cost:", total_cost)
pennies = total_cost * 100
remainder = pennies % 5

if remainder < 2.5:
    rounded_pennies = pennies - remainder
else:
    rounded_pennies = pennies + (5 - remainder)

cash_payment = rounded_pennies / 100

print("Total cost if paid with cash", cash_payment)