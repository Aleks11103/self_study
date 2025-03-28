from math import sqrt, sin


def my_sqr(num):
    return num**2


def my_cube(num):
    return num**3


def my_sqrt(num):
    return sqrt(num)


def my_abs(num):
    return abs(num)


def my_sin(num):
    return sin(num)


n = int(input())
name = input()
d = {'квадрат': my_sqr, 'куб': my_cube, 'корень': my_sqrt, 'модуль': my_abs,
     'синус': my_sin}
print(d[name](n))
