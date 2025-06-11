n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
temp = 1
count = (n // 2) + 1
if n == 4:
    count -= 1
for c in range(count):
    for j in range(c, m - c):
        if matrix[c][j] == 0:
            matrix[c][j] = temp
            temp += 1
    for i in range(c + 1, n - c - 1):
        if m - c - 1 < 0 or m - c - 1 > m:
            continue
        if matrix[i][m-c-1] == 0:
            matrix[i][m-c-1] = temp
            temp += 1
    for j in range(m - c - 1, -1 + c, -1):
        if matrix[n-c-1][j] == 0:
            matrix[n-c-1][j] = temp
            temp += 1
    for i in range(n - c - 2, 0 + c, -1):
        if c < 0 or c >= m:
            continue
        if matrix[i][c] == 0:
            matrix[i][c] = temp
            temp += 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), sep="", end="")
    print()
