pos = input()
lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
n = 8
x = n - int(pos[1])
y = lst.index(pos[0])
matrix = [["." for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == x or j == y or i + j == x + y or i - j == x - y:
            matrix[i][j] = "*"
matrix[x][y] = "Q"
for line in matrix:
    print(*line)
