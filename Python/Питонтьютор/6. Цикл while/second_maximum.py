#Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
first_max = -1
second_max = -1
n = -1
while n != 0:
    n = int(input('n: '))
    if n > first_max:
        second_max = first_max
        first_max = n
    elif n > second_max:
        second_max = n
print(second_max)