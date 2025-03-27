def print_products(*args):
    lst = [el for el in args if type(el) is str and el != '']
    if len(lst) > 0:
        for i in range(len(lst)):
            print(f"{i + 1}) {lst[i]}")
    else:
        print("Нет продуктов")


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5,
               True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
