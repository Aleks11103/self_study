from fractions import Fraction


n = int(input())
lst = [Fraction(1, el**2) for el in range(1, n + 1)]
print(sum(lst))
