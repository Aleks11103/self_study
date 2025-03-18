import random


lst = list('23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ')
n = int(input())
m = int(input())
res = []
for _ in range(n):
    pas = []
    for _ in range(m):
        i = random.randint(0, len(lst) - 1)
        pas.append(lst[i])
    res.append(''.join(pas))
print('\n'.join(res))
