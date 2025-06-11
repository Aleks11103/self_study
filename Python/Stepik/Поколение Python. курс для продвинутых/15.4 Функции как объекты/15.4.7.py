def sum_digit(n):
    s = str(n)
    return sum([int(el) for el in s])


lst = [int(el) for el in input().split()]
lst.sort()
print(*sorted(lst, key=sum_digit))
