# Вам необходимо сформировать последовательность Трибоначчи(звучит страшно,
# но на самом деле это так...шутка). Это последовательность в которой первые
# три числа - это 1, каждое последующее - это сумма трех предыдущих.
# Часть последовательности:
# 1 1 1 3 5 9 17 31 57
# На вход подается целое число, нужно вывести соответствующее количество
# элементов последовательности в одну строку через пробел(как в примере).
n = int(input())
if n > 3:
    print("1 1 1", end="")
    n1, n2, n3 = (1, 1, 1)
    for _ in range(3, n):
        n1, n2, n3 = n2, n3, n1 + n2 + n3
        print(" " + str(n3), end="")
elif n == 3:
    print("1 1 1")
elif n == 2:
    print("1 1")
elif n == 1:
    print("1")
