# У вас есть двумерный список lst. Вам нужно вывести вложенные списки,
# которые соответствуют одному из следующих условий:

# 1. Первый элемент - строка, четвертый - список,
# общее количество элементов неизвестно.

# 2. Четвертый элемент - словарь, последний - кортеж,
# общее количество элементов неизвестно

# вводные данные(не изменять)
lst = [['ого_поймал', 5, 6.6, ['парящая', 'в небе', 'бензопила'], (6, 4, 8)],
       [1, 2, 3, {'1': 'виноград'}, 65.56, 'лимбо', (4, 5, 7)]]

# продолжите решение здесь(в lst вложенные списки)
for el in lst:
    match el:
        case [str(), _, _, list(), *_]:
            print(el)
        case [_, _, _, dict(), *_, tuple()]:
            print(el)
