def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Error: Denominator cannot be zero.")
            return

        reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)
        print(f"The reduced fraction is: {reduced_numerator}/{reduced_denominator}")

    except ValueError:
        print("Error: Please enter valid integers for the numerator and denominator.")

main()
