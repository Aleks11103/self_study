f = open('numbers.txt', encoding='UTF8')
lst = [int(el) for el in f.readlines()]
print(sum(lst))
