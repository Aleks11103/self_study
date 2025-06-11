lst = input().split()
n = int(input())
res = [[] for _ in range(n)]
for i in range(len(lst)):
    res[i % n].append(lst[i])
print(res)
