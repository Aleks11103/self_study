# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов,
# имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят
# единицы. Каждое число равно сумме двух расположенных над ним чисел.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число n. Напишите программу, которая возвращает
# указанную строку треугольника Паскаля в виде списка
# (нумерация строк начинается с нуля).

# Формат входных данных
# На вход программе подается число n (n≥0).

# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.

# Примечание 1. Решение удобно оформить в виде функции pascal(), которая
# принимает номер строки и возвращает соответствующую строку треугольника
# Паскаля.

n = int(input())
lst = [1]
for _ in range(n):
    res = [1]
    for i in range(1, len(lst)):
        res.append(lst[i - 1] + lst[i])
    res.append(1)
    lst = res
print(lst)
