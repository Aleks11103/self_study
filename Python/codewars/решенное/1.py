# В этом ката вы создадите функцию, которая берет список неотрицательных целых
# чисел и строк и возвращает новый список с отфильтрованными строками.

# Пример
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(lst):
    new_l = []
    for el in lst:
        if isinstance(el, int):
            new_l.append(el)
    return new_l


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
