#По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
n = int(input('n: '))
fact = 1
sum = 0
for i in range(1, n + 1):
    fact *= i
    sum += fact
print(sum)