from decimal import Decimal


a = 123
a = a + 456
a = a - 456
a = a / 456
a = a * 456
a = a ** 3
a = 123123123123123123123123123122222222222222222233

a = 0.5

print(a)

a = Decimal('0.1') + Decimal('0.2')

assert a == Decimal('0.3')
print(round(1.33, 1))
import math

print(1 * math.pi)

import random

random.seed("для ")
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))