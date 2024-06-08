q = int(input("Enter a number"))
result = ""
while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print(result)

        



