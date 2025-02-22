#Определите среднее значение всех элементов последовательности, завершающейся числом 0.
n = int(input('n: '))
summa = 0
count = 0
while n != 0:
    summa += n
    count += 1
    n = int(input('n: '))
if count == 0:
    print(0)
else:
    print(summa / count)