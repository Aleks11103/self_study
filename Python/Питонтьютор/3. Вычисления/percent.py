#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год.
#Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
p = int(input('проценты: '))
x = int(input('рубли: '))
y = int(input('копейки: '))

m = int((x * 100 + y) * (100 + p) / 100)
print(m // 100, m % 100)