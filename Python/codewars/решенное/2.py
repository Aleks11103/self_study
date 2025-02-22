# В этом небольшом задании вам дается строка чисел, разделенных пробелами, и вы должны вернуть наибольшее и наименьшее число.

# Примеры
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"


def high_and_low(numbers):
    l = [int(i) for i in numbers.split()]
    n_max = max(l)
    n_min = min(l)
    s = str(n_max) + " " + str(n_min)
    return s


print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))