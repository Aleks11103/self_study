import random

length = int(input())    # длина пароля
for _ in range(length):
    print(chr(random.randint(65, 90) + random.randrange(0, 32, 31)), end='')
