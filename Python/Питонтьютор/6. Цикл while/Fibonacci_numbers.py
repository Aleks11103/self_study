#Последовательность Фибоначчи определяется так:
#φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#По данному числу n определите n-е число Фибоначчи φn.
#Эту задачу можно решать и циклом for.
n = int(input('n: '))
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    i = 2
    prev_1 = 0
    prev_2 = 1
    while i <= n:
        fib = prev_1 + prev_2
        prev_2, prev_1 = fib, prev_2
        i += 1
    print(prev_2)