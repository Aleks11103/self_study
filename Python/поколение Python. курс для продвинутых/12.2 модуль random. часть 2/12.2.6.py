import random


lst = [x for x in range(1, 75)]
random.shuffle(lst)
matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 2 and j == 2:
            continue
        else:
            matrix[i][j] = lst[5 * i + j]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]}".ljust(3), end="")
    print()
