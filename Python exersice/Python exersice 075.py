m = int(input())
n = int(input())
d = min(n, m)
while n % d != 0 or m % d != 0:
    d -= 1
print("The greatest common divisor of", n, "and", m, "is", d)

        



