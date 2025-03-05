d = {}
for _ in range(int(input())):
    name, *oper = input().split()
    d[name] = oper
for _ in range(int(input())):
    oper, file = input().split()
    if oper == 'execute':
        print('OK') if 'X' in d[file] else print('Access denied')
    elif oper == 'write':
        print('OK') if 'W' in d[file] else print('Access denied')
    elif oper == 'read':
        print('OK') if 'R' in d[file] else print('Access denied')
