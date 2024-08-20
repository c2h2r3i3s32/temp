import math
t = int(input("Enter air temperatures"))
s = int(input("Enter wind speed"))
print('WCI=', 13.12 + 0.6215 * t - 11.37 * s ** 0.16 + 0.3965 * s ** 0.16)