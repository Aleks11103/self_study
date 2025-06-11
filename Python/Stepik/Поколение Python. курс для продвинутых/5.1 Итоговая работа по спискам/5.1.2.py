n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
max_el = matrix[0][-1]
for i in range(n):
    for j in range(n):
        if j >= n - i - 1 and matrix[i][j] > max_el:
            max_el = matrix[i][j]
print(max_el)
