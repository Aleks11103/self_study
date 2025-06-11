f = open('nums.txt', encoding='UTF8')
lst = filter(None, [el.strip() for el in f.readlines()])
lst = map(int, lst)
print(sum(lst))
