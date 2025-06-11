def evaluete(coef, x):
    n = len(coef) - 1
    i = 0
    res = 0
    while i <= n:
        res += coef[i] * x**(n-i)
        i += 1
    return res


lst = [int(x) for x in input().split()]
x = int(input())
print(evaluete(lst, x))
