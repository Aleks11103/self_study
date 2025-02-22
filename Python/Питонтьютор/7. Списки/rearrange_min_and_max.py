#В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(i) for i in input().split()]
min_elem = min(a)
max_elem = max(a)
min_index = a.index(min_elem)
max_index = a.index(max_elem)
a[max_index], a[min_index] = a[min_index], a[max_index]
print(*a)