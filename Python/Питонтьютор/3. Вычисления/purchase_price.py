a = int(input('Рубли:'))
b = int(input('Копейки: '))
n = int(input('Количество: '))

print(a * n + b * n // 100, b * n % 100)