m = (input("Enter the month"))
month = {"January": 31, "February": "28 or 29", "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
if m in month:
    print(month.get(m))
