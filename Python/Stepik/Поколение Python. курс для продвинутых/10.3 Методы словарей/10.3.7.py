lst = input().split()
d = {}
res = []
for el in lst:
    if el in d:
        res.append(f"{el}_{d[el]}")
        d[el] += 1
    else:
        res.append(el)
        d[el] = 1
print(*res)
