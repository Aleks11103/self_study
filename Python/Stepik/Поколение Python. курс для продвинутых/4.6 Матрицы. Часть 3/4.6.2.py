n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            matrix[i][j] = 1
        elif j > n - i - 1:
            matrix[i][j] = 2
for line in matrix:
    print(*line)
