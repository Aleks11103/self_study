n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for line in matrix:
    print(*line)
