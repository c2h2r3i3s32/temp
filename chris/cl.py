inserted_money = 0
price = 0
Drink = {1: 1.00, 2: 1.50, 3: 2.00}
select = 0
totalmoney = 0
leftmoney = 0

def menu(): 
    print('''
        --- Vending Machine Menu ---
        1: Water ($1.00)
        2: Soda ($1.50)
        3: Coffee ($2.00)
        4: Quit
        Please select a drink (Input 1-4):
    ''')

while True:
    menu()
    try:
        select = int(input("Select a drink: "))
    except ValueError:
        print("Invalid input, please enter a number.")

    if select == 4:
        print("Goodbye")
        break

    elif select >= 1 and select <= 3: 
        price = Drink[select] 
        inserted_money = float(input("Insert money: "))       
        totalmoney += inserted_money

        while totalmoney < price:
            leftmoney = totalmoney - price
            print("Inserted:", totalmoney, "left:", leftmoney)
            more_money = float(input("insert more money: "))
            totalmoney += more_money

        if totalmoney >= price:
            change = totalmoney - price
            print(f"Enjoy your drink, Returning change: ${change:.2f}")

    else:
        print("Choose between 1 and 4.")

