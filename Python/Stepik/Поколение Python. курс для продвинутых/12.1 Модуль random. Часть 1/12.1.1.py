import random

n = int(input())    # количество попыток
for i in range(n):
    if random.randint(0, 1):
        print('Орел')
    else:
        print('Решка')
