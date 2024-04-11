import json
transactions = []

def input_transaction():
    date = input("Enter transaction date (YYYY-MM-DD): ")
    transaction_type = input("Enter transaction type (income/expense): ")
    category = input("Enter transaction category: ")
    amount = input("Enter transaction amount: ")   
    transaction = {'date': date, 'type': transaction_type, 'category': category, 'amount': amount}   
    transactions.append(transaction)
    print("Transaction added successfully!")

def display_summary():
    income_list = []
    expense_list = []
    for transaction in transactions:
        if transaction['type'] == 'income':
            income_list.append(transaction)
            print('income:\n', income_list)
        
        else:
            print("No income found.")
        
    for transaction in transactions:
        if transaction['type'] == 'expense':
            expense_list.append(transaction)
            print('expense:\n', expense_list) 
        
        else:
            print("No expense found.")
         

def search_transactions():
    search = input("Enter 'date' or 'category' to search transactions: ")
    if search not in ['date', 'category']:
        print("Invalid search!")
        return
    
    search_term = input(f"Enter {search}: ")
    
    found_transactions = []
    for transaction in transactions:
        if transaction[search] == search_term:
            found_transactions.append(transaction)
        else:
            print("No transactions found.")
    print(found_transactions)

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Input Transaction")
        print("2. Display Summary")
        print("3. Search Transactions")    
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_transaction()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            search_transactions()
        else:
            print("Invalid choice!")

main()
     