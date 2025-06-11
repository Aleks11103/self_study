lst = [el.strip('.,!?:;-') for el in input().lower().split()]
d = {}
for el in lst:
    d[el] = d.get(el, 0) + 1
min_count = min(d.values())
ans = [key for key, value in d.items() if value == min_count]
print(min(ans))
