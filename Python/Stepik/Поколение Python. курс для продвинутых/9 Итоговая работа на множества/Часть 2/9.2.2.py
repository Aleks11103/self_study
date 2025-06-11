lst = [int(x) for x in input().split()]
s = set(lst)
print(len(lst) - len(s))
