# Дан список сотрудников фирмы. В нем лежат данные работников в виде словарей.
# Данный вариант списка предназначен для начальства. А сотрудникам подается
# этот же список, но в котором в словарях не будет параметра "salary".
# На экран вывести измененный список.

# вводные данные(не изменять)
employees = [
    {
        'name': 'Alex',
        'position': 'director',
        'salary': 1000000
    },
{
        'name': 'Marty',
        'position': 'security',
        'salary': 50000
    },
{
        'name': 'Gloria',
        'position': 'accountant',
        'salary': 150000
    }
]

# продолжите решение здесь
res = employees.copy()
for el in res:
    del el["salary"]
print(res)
