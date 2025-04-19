res = []
for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        lst.append(tuple(input().split()))
    res.append(True if any(map(lambda x: x[1] == '5', lst)) else False)
print('YES' if all(res) else 'NO')
