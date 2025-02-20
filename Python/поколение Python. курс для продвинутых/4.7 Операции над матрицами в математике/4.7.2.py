n1, m1 = map(int, input().split())
matr_1 = [[int(x) for x in input().split()] for _ in range(n1)]
input()
n2, m2 = map(int, input().split())
matr_2 = [[int(x) for x in input().split()] for _ in range(n2)]
matr_3 = [[0 for j in range(m2)] for i in range(n1)]
for i in range(m2):
    line_mat_1 = matr_1[i]
    for j in range(n1):
        line_mat_2 = []
        for k in range(n2):
            line_mat_2.append(matr_2[k][j])
        res = 0
        for ind in range(len(line_mat_1)):
            res = res + line_mat_1[ind] * line_mat_2[ind]
        matr_3[i][j] = res
for line in matr_3:
    print(*line)
