set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])
print(*sorted(set_1 & set_2))
