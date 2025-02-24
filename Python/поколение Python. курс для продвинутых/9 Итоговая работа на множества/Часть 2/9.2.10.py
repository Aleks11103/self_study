m = int(input())
n = int(input())
res_set = set()
for _ in range(m + n):
    s = input()
    if s in res_set:
        res_set.discard(s)
    else:
        res_set.add(s)
print(len(res_set)) if len(res_set) > 0 else print("NO")
