n = int(input())
d = {}
for _ in range(n):
    num, name = input().split()
    if name in d:
        d[name].append(num)
    else:
        d[name] = [num]
m = int(input())
for _ in range(m):
    s = input().capitalize()
    if s in d:
        print(*d[s])
    else:
        print('абонент не найден')
