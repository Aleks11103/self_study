import random


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
lst = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        lst.append(matrix[i][j])
random.shuffle(lst)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = lst[i * len(matrix) + j]
for line in matrix:
    print(*line)
