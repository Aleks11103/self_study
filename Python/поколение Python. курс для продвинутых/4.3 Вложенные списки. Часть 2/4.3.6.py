# На вход программе подаются две строки: на одной – символы,
# на другой – число n. Из первой строки формируется список.

# Реализуйте функцию chunked(), которая принимает на вход список и число,
# задающее размер чанка (куска), а возвращает список из чанков (кусков)
# указанной длины.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные
# символом пробела и число n на отдельной строке.

# Формат выходных данных
# Программа должна вывести указанный вложенный список.

# Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат.

def chunked(lst, n):
    res = []
    for i in range(len(lst) // n):
        temp_lst = []
        for el in lst[i*n:i*n + n]:
            temp_lst.append(el)
        res.append(temp_lst)
    else:
        if len(lst) % n != 0:
            res.append(lst[-1 * (len(lst) % n):])
    return res


lst = input().split()
n = int(input())
print(chunked(lst, n))
