n = int(input("Введите количество чисел последовательности Фибоначчи: "))
l = [1, 1]
if n == 1:
    print(1)
else:
    for i in range(2, n):
        l.append(l[-1] + l[-2])
print(*l)