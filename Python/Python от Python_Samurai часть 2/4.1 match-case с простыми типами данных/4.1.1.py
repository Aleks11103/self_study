# Дан список различных типов данных, вам необходимо перебрать его и для каждого
# типа данных, кроме str, вывести информацию:

# Это тип данных - <class '<тип>'>

# вводные данные
lst = [1, 5.6, '3', [1, 2], (4, 7), {'a': 4}, True]

# продолжите решение здесь
for el in lst:
    if isinstance(el, str):
        pass
    else:
        print(f"Это тип данных - {type(el)}")
