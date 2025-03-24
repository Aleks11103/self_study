from fractions import Fraction
from math import factorial


n = int(input())
lst = [Fraction(1, factorial(el)) for el in range(1, n + 1)]
print(sum(lst))
