#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
n = -1
count = 1
maximum = -1
while n != 0:
    n = int(input('n: '))
    if n > maximum:
        maximum = n
        count = 1
    elif n == maximum:
        count +=1
print(count)