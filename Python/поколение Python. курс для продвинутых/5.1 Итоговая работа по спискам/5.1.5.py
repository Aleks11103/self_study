n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
flag = False
for i in range(n):
    if flag:
        break
    for j in range(n - i):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            flag = True
            print("NO")
            break
else:
    print("YES")
