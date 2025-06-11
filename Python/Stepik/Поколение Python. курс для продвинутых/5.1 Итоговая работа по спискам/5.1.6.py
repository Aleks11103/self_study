n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
lst = [x for x in range(1, n + 1)]
for i in range(n):
    row = sorted(matrix[i])
    column = []
    for j in range(n):
        column.append(matrix[j][i])
    column.sort()
    if lst != row or lst != column:
        print("NO")
        break
else:
    print("YES")
