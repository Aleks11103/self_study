# Дан список с вложенными списками имен сотрудников компании. Это своего рода
# недельный отчет о посещаемости сотрудниками работы. Каждый вложенный
# список(ежедневный отчет) - это фиксация камерами сотрудников, пришедших на
# работу(стоит учитывать, что в течение дня они могут покидать рабочее место и
# возвращаться). Необходимо узнать кто из сотрудников не приходил на работу
# более 1 раза в течение недели. Также известно, что в течение недели каждый
# сотрудник приходил на работу хотя бы 1 раз. Вывести данных сотрудников и
# количество пропущенных ими рабочих дней в алфавитном порядке в формате:

# <Имя Фамилия>: <количество> | <Имя Фамилия>: <количество> |
# <Имя Фамилия>: <количество>

# вводные данные
employees = [
    ['Алексей К.', 'Владимир О.', 'Ульяна П.', 'Кирилл Р.', 'Анна С.',
     'Марат М.', 'Ульяна П.', 'Олег В.', 'Ульяна П.'],
    ['Никита Д.', 'Владимир О.', 'Кирилл Р.', 'Анна С.', 'Марат М.',
     'Ульяна П.', 'Олег В.', 'Никита Д.', 'Владимир О.'],
    ['Алексей К.', 'Владимир О.', 'Кирилл Р.', 'Анна С.', 'Марат М.',
     'Ульяна П.', 'Олег В.', 'Никита Д.', 'Елена Р.', 'Олег Р.', 'Кирилл Р.',
     'Кирилл Р.'],
    ['Олег В.', 'Никита Д.', 'Елена Р.', 'Олег Р.', 'Владимир О.', 'Кирилл Р.',
     'Анна С.'],
    ['Алексей К.', 'Владимир О.', 'Кирилл Р.', 'Анна С.', 'Марат М.',
     'Ульяна П.', 'Олег В.', 'Никита Д.', 'Елена Р.', 'Олег Р.', 'Владимир О.',
     'Кирилл Р.', 'Анна С.'],
    ['Алексей К.', 'Кирилл Р.', 'Анна С.', 'Марат М.', 'Ульяна П.', 'Олег В.',
     'Никита Д.', 'Елена Р.', 'Олег Р.'],
    ['Алексей К.', 'Владимир О.', 'Кирилл Р.', 'Анна С.', 'Марат М.',
     'Ульяна П.', 'Олег В.', 'Никита Д.', 'Анна С.', 'Олег Р.', 'Кирилл Р.']
]

# продолжите решение здесь
s = set()
for day in employees:
    for el in day:
        s.add(el)
d = {x: 7 for x in s}
for day in employees:
    for el in set(day):
        d[el] -= 1
res = []
for name in sorted(d.keys()):
    if d[name] > 1:
        res.append(f'{name}: {d[name]}')
print(' | '.join(res))
