from fractions import Fraction


n = int(input())
lst = set([Fraction(i, j) for j in range(1, n + 1) for i in range(1, j)])
print(*sorted(lst), sep='\n')
