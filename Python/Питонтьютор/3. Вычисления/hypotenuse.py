#Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
from math import sqrt
a = int(input('a: '))
b = int(input('b: '))
print(sqrt(a * a + b * b))