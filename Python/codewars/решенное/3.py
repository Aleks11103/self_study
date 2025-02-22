# Возможно, вы знаете несколько довольно больших идеальных квадратов. Но как насчет СЛЕДУЮЩЕГО?

# Выполните метод find Next Square, который находит следующий интегральный совершенный квадрат после переданного в качестве параметра. Напомним, что интегральный совершенный квадрат - это целое число n, такое, что sqrt (n) также является целым числом.

# Если параметр сам по себе не является идеальным квадратом, то следует вернуть значение -1. Вы можете предположить, что параметр неотрицательный.

# Examples:(Input --> Output)
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square
from math import sqrt


def find_next_square(sq):
    if int(sqrt(sq)) - sqrt(sq) == 0:
        n = sqrt(sq) + 1
        return int(n ** 2)
    else:
        return -1


print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))