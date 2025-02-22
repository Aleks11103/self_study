#Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
max_len = 0
temp_len = 0
prev_elem = 0
n = -1
while n != 0:
    prev_elem = n
    n = int(input('n: '))
    if prev_elem == n:
        temp_len += 1
    else:
        if temp_len > max_len:
            max_len = temp_len
        temp_len = 1
print(max_len)