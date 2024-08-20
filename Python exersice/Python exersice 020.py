pressure = int(input("Enter the pressure"))
volume = int(input("Enter the volume" ))
temperature = int(input("Enter the temperature"))
T = temperature + 273.15
n = pressure * volume / 8.314 / T
print("The amount of gas in moles is", n)