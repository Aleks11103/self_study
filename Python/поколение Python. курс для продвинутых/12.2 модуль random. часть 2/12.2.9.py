import random


lst = list('23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ')
n = int(input())
m = int(input())
res = []
while len(res) < n:
    f_num = False
    f_upp_letter = False
    f_low_letter = False
    pas = []
    for _ in range(m):
        i = random.randint(0, len(lst) - 1)
        c = lst[i]
        if c in '23456789':
            f_num = True
        elif c in 'abcdefghijkmnpqrstuvwxyz':
            f_low_letter = True
        else:
            f_upp_letter = True
        pas.append(c)
    if f_num and f_upp_letter and f_low_letter:
        res.append(''.join(pas))
print('\n'.join(res))
