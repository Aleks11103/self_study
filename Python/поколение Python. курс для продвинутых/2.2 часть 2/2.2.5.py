# На вход программе подается строка текста, содержащая натуральные числа,
# расположенные по неубыванию. Из строки формируется список чисел.
# Напишите программу для подсчета количества разных элементов в списке.

# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа,
# разделенные символом пробела, расположенные по неубыванию.

# Формат выходных данных
# Программа должна вывести одно число – количество различных элементов списка.

s = set([int(x) for x in input().split()])
print(len(s))
