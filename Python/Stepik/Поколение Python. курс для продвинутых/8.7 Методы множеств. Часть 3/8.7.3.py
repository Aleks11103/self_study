set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])
set_3 = set([int(x) for x in input().split()])
join_set = set_1 & set_2
res = join_set - set_3
print(*sorted(res, reverse=True))
