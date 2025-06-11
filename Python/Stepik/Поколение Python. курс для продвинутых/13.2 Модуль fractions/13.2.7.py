from fractions import Fraction


n = int(input())
lst = [Fraction(i, n - i) for i in range(1, (n + 1) // 2)]
for el in lst[-1::-1]:
    if el.numerator + el.denominator == n:
        print(el)
        break
