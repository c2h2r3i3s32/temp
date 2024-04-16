cents = int(input("Enter the amount of cents: "))
change = []
denominations = (200, 100, 25, 10, 5, 1)
for i in denominations:
  if i >= cents:
    cents = cents - i   
    change.append(i)
  
  elif i = 0
  print(change)