#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.

#Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(j) for j in input().split()]
    x.append(new_x)
    y.append(new_y)

flag = True
for i in range(n - 1):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            flag = False

if flag == True:
    print('NO')
else:
    print('YES')