n = int(input())
matrix_a = [[int(x) for x in input().split()] for _ in range(n)]
step = int(input())  # Степень матрицы
matrix_b = matrix_a.copy()
for _ in range(step - 1):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix_a[i][k] * matrix_b[k][j]
    matrix_b = res.copy()
for line in matrix_b:
    print(*line)
