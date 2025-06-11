d = {}
lst = [el for el in input().split()]
for el in lst:
    d[el] = d.get(el, 0) + 1
    print(d[el], end=' ')
