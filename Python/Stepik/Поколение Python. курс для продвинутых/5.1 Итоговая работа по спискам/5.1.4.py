n = int(input())
lst = [["." for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i == n // 2 or j == n // 2:
            lst[i][j] = "*"
for line in lst:
    print(*line)
