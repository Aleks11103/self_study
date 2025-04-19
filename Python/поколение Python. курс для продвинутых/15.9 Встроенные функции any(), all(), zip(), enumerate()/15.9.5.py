a = int(input())
b = int(input())
lst = [el for el in range(a, b + 1) if '0' not in str(el)]
res = []
for el in lst:
    s = str(el)
    for c in s:
        if el % int(c) != 0:
            break
    else:
        res.append(el)
print(*res)
