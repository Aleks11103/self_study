n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
temp = 1
for x in range(m + n):
    for y in range(n):
        if 0 <= x-y < m and 0 <= y < n:
            matrix[y][x-y] = temp
            temp += 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), sep="", end="")
    print()
