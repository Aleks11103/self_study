n = int(input())
lst = []
for _ in range(n):
    name, count = input().split()
    lst.append((name, int(count)))
for el in lst:
    print(*el)
print()
for name, count in lst:
    if count >= 4:
        print(name, count)
