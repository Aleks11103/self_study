#Определите количество четных элементов в последовательности, завершающейся числом 0.
count = 0
n = int(input('n: '))
while n != 0:
    if n % 2 == 0:
        count += 1
    n = int(input('n: '))
print(count)