#Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.
n = int(input('n: '))
if n == 0:
    print(0)
else: 
    i = 1
    prev_1 = 0
    prev_2 = 1
    flag = False
    while prev_1 + prev_2 <= n:
        fib = prev_1 + prev_2
        prev_2, prev_1 = fib, prev_2
        i += 1
        if n == fib:
            flag = True
    if flag:
        print(i)
    else:
        print(-1)