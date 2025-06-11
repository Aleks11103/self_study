d1 = {}
d2 = {}
s1 = input().lower()
s2 = input().lower()
for el in s1:
    if el not in d1:
        d1[el] = 1
    else:
        d1[el] += 1
for el in s2:
    if el not in d2:
        d2[el] = 1
    else:
        d2[el] += 1
print('YES') if d1 == d2 else print('NO')
