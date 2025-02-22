from math import ceil
h = int(input('Высота: '))
a = int(input('a: '))
b = int(input('b: '))

print(ceil((h - a) / (a - b)) + 1)