#Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
a = input().split()
for i in a:
    if int(i) % 2 == 0:
        print(i, end=' ')