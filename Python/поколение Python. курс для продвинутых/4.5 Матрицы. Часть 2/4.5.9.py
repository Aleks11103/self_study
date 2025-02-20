# Магическим квадратом порядка n называется квадратная таблица размера n×n,
# составленная из всех чисел 1,2,3, …, n**2 так, что суммы по каждому столбцу,
# каждой строке и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет, является ли заданная квадратная
# матрица магическим квадратом.

# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов
# в матрице, затем элементы матрицы: n строк, по n чисел в каждой,
# разделенные пробелами.

# Формат выходных данных
# Программа должна вывести YES, если матрица является магическим квадратом,
# или NO в противном случае.

n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
flag = True
main_diag = 0
sec_diag = 0
rows = [0 for i in range(n)]
columns = [0 for i in range(n)]
mag_lst = [x for x in range(1, n**2 + 1)]
for i in range(n):
    main_diag += matrix[i][i]
    sec_diag += matrix[i][n - i - 1]
    for j in range(n):
        columns[j] += matrix[i][j]
        if matrix[i][j] in mag_lst:
            mag_lst.remove(matrix[i][j])
    rows[i] = sum(matrix[i])
for i in range(n):
    print(main_diag, sec_diag, columns, rows, sep="\n")
    if main_diag != rows[i] or main_diag != columns[i]:
        flag = False
if flag and main_diag == sec_diag and not mag_lst:
    print("YES")
else:
    print("NO")
