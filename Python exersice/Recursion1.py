series = []
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_series(n):
    for i in range(n):
        series.append(fib(i))
    return series

n = 5
output = fib_series(n)
print("Fibonacci series of", n, "numbers is:", series)
