import math
a = int(input())
b = int(input())
print('The sum of a and b is {0}\n'
      'The difference when b is subtracted from a is {1}\n'
      'The product of a and b is {2}\n'
      'The quotient when a is divided by b is {3}\n'
      'The remainder when a is divided by b is {4}\n'
      'The result of log10 a is {5}\n'
      'The result of a^b is {6}'.format(a + b, a - b, a * b, a / b, a % b, math.log10(a), a ** b))

