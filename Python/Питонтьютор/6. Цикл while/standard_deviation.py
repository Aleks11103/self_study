#Дана последовательность натуральных чисел x1, x2, ..., xn. Стандартным отклонением называется величина
#σ = √((x1−s)2+(x2−s)2+…+(xn−s)2) / (n−1)
#где s = (x1 + x2 + … + xn) / n — среднее арифметическое последовательности.
#Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
from math import sqrt
 
partial_sum = 0
partial_sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partial_sum += x_i
    partial_sum_squares += x_i ** 2
    x_i = int(input())
print(sqrt((partial_sum_squares - partial_sum ** 2 / n) / (n - 1)))