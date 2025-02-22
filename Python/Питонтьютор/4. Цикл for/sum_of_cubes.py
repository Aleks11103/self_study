#По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.
n = int(input('n: '))
sum = 0
for i in range(1, n + 1):
    sum += pow(i, 3)
print(sum)