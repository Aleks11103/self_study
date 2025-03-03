d1 = {}
d2 = {}
lst1 = [el.strip('.,!?:;-') for el in input().lower().split()]
lst2 = [el.strip('.,!?:;-') for el in input().lower().split()]
for s in lst1:
    for el in s:
        if el not in d1:
            d1[el] = 1
        else:
            d1[el] += 1
for s in lst2:
    for el in s:
        if el not in d2:
            d2[el] = 1
        else:
            d2[el] += 1
print('YES') if d1 == d2 else print('NO')
