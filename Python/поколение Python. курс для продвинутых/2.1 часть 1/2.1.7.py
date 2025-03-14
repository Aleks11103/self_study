# На вход программе подаётся натуральное число. Напишите программу,
# которая вставляет в заданное число запятые в соответствии со стандартным
# американским соглашением о запятых в больших числах.

# Формат входных данных
# На вход программе подается натуральное число
# n(0 < n < 10^100).

# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с условием задачи.

s = input()
lst = []
i = 0
while i <= len(s) // 3 - 1:
    lst.append(s[-3:])
    s = s[:-3]
if len(s) > 0:
    lst.append(s)
lst.reverse()
print(",".join(lst))
