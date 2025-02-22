n = int(input("Введите предел последовательности: "))
l = []
for i in range(n + 1):
    if i % 5 == 3:
        l.append(i)
print(*l)
print(*l[::-1])