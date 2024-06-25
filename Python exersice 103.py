def is_magic_date(day, month, year):
    year_two_digits = year % 100
    return day * month == year_two_digits

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                days_in_month = 31
            elif month in [4, 6, 9, 11]:
                days_in_month = 30
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            
            for day in range(1, days_in_month + 1):
                if is_magic_date(day, month, year):
                    print(f"Magic Date: {month}/{day}/{year}")

main()
