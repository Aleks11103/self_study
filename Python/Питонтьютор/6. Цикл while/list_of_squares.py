#По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
n = int(input())
i = 1
while i * i <= n:
    print(i * i, end=' ')
    i += 1