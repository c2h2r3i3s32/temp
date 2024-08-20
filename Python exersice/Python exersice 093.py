def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    return True

def nextPrime(n):
    nextprime = n + 1
    while not is_prime(nextprime):
        nextprime += 1
    return nextprime

n = int(input("Enter an integer: "))
prime = nextPrime(n)
print(f"The first prime number larger than {n} is {prime}.")
