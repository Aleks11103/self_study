lst = [int(el) for el in input().split('.') if el.isdigit() and
       0 <= int(el) <= 255]
print(len(lst) == 4)
