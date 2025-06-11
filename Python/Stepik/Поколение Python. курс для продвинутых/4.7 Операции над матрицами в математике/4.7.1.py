n, m = map(int, input().split())
matrix_1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
matrix_2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix_3 = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
for line in matrix_3:
    print(*line)
