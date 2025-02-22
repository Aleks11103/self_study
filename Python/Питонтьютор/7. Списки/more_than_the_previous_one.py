#Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

a = input().split()
for i in a:
    int(i)
for i in range(1, len(a)):
    if a[i - 1] < a[i]:
        print(a[i], end=' ')