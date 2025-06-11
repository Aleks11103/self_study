from fractions import Fraction


s1 = input()
s2 = input()
print(f"{s1} + {s2} = {Fraction(s1) + Fraction(s2)}")
print(f"{s1} - {s2} = {Fraction(s1) - Fraction(s2)}")
print(f"{s1} * {s2} = {Fraction(s1) * Fraction(s2)}")
print(f"{s1} / {s2} = {Fraction(s1) / Fraction(s2)}")
