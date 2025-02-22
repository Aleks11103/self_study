# Нарциссическое число - это положительное число, представляющее собой сумму собственных цифр, каждая из которых возведена в степень числа цифр в данной базе. В этом Ката мы ограничимся десятичной дробью (основание 10).

# Например, возьмем 153 (3 цифры), что является нарциссическим:

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# и 1652 (4 цифры), что не является:

# 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# Задача:

# Ваш код должен возвращать значение true или false (не "true" и "false") в зависимости от того, является ли данное число нарциссическим числом в базе 10. Это может быть True и False на вашем языке, например, PHP.

# Проверка ошибок на наличие текстовых строк или других недопустимых входных данных не требуется, в функцию будут передаваться только допустимые положительные ненулевые целые числа.


def narcissistic(value):
    step = len(str(value))
    s = 0
    for i in str(value):
        s += int(i) ** step
    if s == value:
        return True
    else:
        return False


print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))