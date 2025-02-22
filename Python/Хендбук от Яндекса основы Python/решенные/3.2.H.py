n = int(input())
d = {}

for _ in range(n):
    lst = input().split()
    for el in lst[1:]:
        if el in d:
            d[el].append(lst[0])
        else:
            d[el] = [lst[0]]

s = input()
if s in d:
    print("\n".join(sorted(d[s])))
else:
    print("Таких нет")
