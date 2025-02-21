set_1 = set([int(x) for x in input().split()])
set_2 = set([int(x) for x in input().split()])
set_3 = set([int(x) for x in input().split()])
all_elem = set().union(set_1, set_2, set_3)
res = set()
for el in all_elem:
    if (el in set_1 or el in set_2) and el not in set_3:
        res.add(el)
    elif (el in set_1 or el in set_3) and el not in set_2:
        res.add(el)
    elif (el in set_2 or el in set_3) and el not in set_1:
        res.add(el)
print(*sorted(res))
