#Дано действительное положительное число a и целоe число n.
#Вычислите an. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    if n == 0:
        res = 1
    elif n > 0:
        res = a
        for i in range(1, n):
            res *= a
    else:
        res = 1 / a
        for i in range(1, abs(n)):
            res = res * (1 / a)
    return res

a = float(input())
n = int(input())

print(power(a, n))