def sum_digit(s):
    return sum([int(el) for el in s])


lst = input().split()
print(*sorted(lst, key=sum_digit))
