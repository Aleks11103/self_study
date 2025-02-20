# Напишите программу, которая меняет местами столбцы в матрице.

# Формат входных данных
# На вход программе на разных строках подаются два натуральных числа n и m —
# количество строк и столбцов в матрице, затем элементы матрицы построчно через
# пробел, затем натуральные числа i и # j — номера столбцов, подлежащих обмену.

# Формат выходных данных
# Программа должна вывести указанную таблицу с замененными столбцами.

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
sw_1, sw_2 = map(int, input().split())
for line in matrix:
    line[sw_1], line[sw_2] = line[sw_2], line[sw_1]
for line in matrix:
    print(*line)
