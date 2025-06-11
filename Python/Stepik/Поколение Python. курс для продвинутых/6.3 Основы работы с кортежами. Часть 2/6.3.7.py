n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    res = [1, 1, 1]
    for _ in range(3, n):
        new_num = res[-1] + res[-2] + res[-3]
        res.append(new_num)
    print(*res)
