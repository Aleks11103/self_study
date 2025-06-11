def f1(tpl):
    return tpl[0]


def f2(tpl):
    return tpl[1]


def f3(tpl):
    return tpl[2]


def f4(tpl):
    return tpl[3]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
            ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = input()
d = {'1': f1, '2': f2, '3': f3, '4': f4}
athletes.sort(key=d[n])
for el in athletes:
    print(*el)
