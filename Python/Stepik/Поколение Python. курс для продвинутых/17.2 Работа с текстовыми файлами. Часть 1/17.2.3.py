from random import randint


f = open('lines.txt', encoding='UTF8')
lst = f.readlines()
print(lst[randint(0, len(lst) - 1)])
