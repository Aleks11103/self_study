# Дана квадратная матрица чисел. Напишите программу, которая меняет местами
# элементы, стоящие на главной и побочной диагонали, при этом каждый элемент
# должен остаться в том же столбце (то есть в каждом столбце нужно поменять
# местами элемент на главной диагонали и на побочной диагонали).

# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов
# в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести матрицу с элементами главной и побочной диагонали,
# поменявшимися своими местами.

n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
for line in matrix:
    print(*line)
