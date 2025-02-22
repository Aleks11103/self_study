# Вам дан словарь dct_1. На вход подается еще один dct_2. Вам необходимо
# дополнить первый словарь вторым. Вывести объединенный словарь dct_1 на экран.
# вводные данные(не изменять)
import sys
dct_1 = {'рука': 'hand'}
dct_2 = {k: v for i in sys.stdin.readlines() for k, v in [i.split()]}

# продолжите решение здесь
for key, value in dct_2.items():
    dct_1[key] = value
print(dct_1)
