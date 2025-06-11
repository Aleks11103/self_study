set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])
set_3 = set([int(x) for x in input().split()])
print(*sorted(set_3 - set_2 - set_1, reverse=True))
