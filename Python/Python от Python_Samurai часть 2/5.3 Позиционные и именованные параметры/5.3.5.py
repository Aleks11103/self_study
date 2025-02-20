# А вдруг всё что мы с вами видим вокруг это всё ненастоящее, симуляция.
# Кто-то более могущественный использует нашу жизненную энергию, рисуя нам мир,
# которого на самом деле нет. По моему неплохой оригинальный сюжет,
# надо отправить его каким-нибудь режиссерам.

# Вам нужно создать функцию func, которая возвращает матрицу(двумерный список,
# в каждом вложенном списке целые числа). Она имеет ключевые параметры
# size=5, up=0, down=0. Напомню, что диагональ матрицы проходит от верхнего
# левого края, до нижнего правого, она должна заполняться 1.
# size отвечает за размер матрицы(5x5 по умолчанию).
# up отвечает за то, какими цифрами мы должны заполнять матрицу выше диагонали,
# down - тоже самое, только ниже диагонали.

# Пример матрицы:

# [
#  1, 0, 0, 0, 0,
#  0, 1, 0, 0, 0,
#  0, 0, 1, 0, 0,
#  0, 0, 0, 1, 0,
#  0, 0, 0, 0, 1,
# ]

def func(size=5, up=0, down=0):
    res = []
    for i in range(size):
        line = []
        for j in range(size):
            if i == j:
                line.append(1)
            elif i < j:
                line.append(up)
            else:
                line.append(down)
        res.append(line)
    return res


print(func())
print(func(size=7))
print(func(size=3, up=3))
