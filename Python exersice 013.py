cents = int(input("Enter the amount of cents: "))
p, c, q, d, t, n = 0, 0, 0, 0, 0, 0
while cents > 0:
  if cents >= 200:
    p = p + 1
    cents = cents - 200
  elif cents >= 100:
    c = c + 1
    cents = cents - 100
  elif cents >= 25:
    q = q + 1
    cents = cents - 25
  elif cents >= 10:
    d = d + 1
    cents = cents - 10
  elif cents >= 5:
    t = t + 1
    cents = cents - 5
  elif cents >= 1:
    n = n + 1
    cents = cents - 1

print(p, 'pennies', c, 'loonies', q, 'quarters', d, 'dimes', t, 'toonies', n, 'nickels')