a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= d:
    if b <= e or c <= e:
        print('YES')
    else:
        print('NO')
elif a <= e:
    if b <= d or c <= d:
        print('YES')
    else:
        print('NO')
elif b <= d:
    if a <= e or c <= e:
        print('YES')
    else:
        print('NO')
elif b <= e:
    if a <= d or c <= d:
        print('YES')
    else:
        print('NO')
elif c <= d:
    if a <= e or b <= e:
        print('YES')
    else:
        print('NO')
else:
    if a <= d or b <= d:
        print('YES')
    else:
        print('NO')