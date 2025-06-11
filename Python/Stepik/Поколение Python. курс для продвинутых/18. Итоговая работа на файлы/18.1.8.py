with open(input(), 'r', encoding='utf-8') as f:
    lst = f.readlines()
    res = []
    for i in range(len(lst)):
        if lst[i].startswith('def '):
            if lst[i - 1].startswith('# '):
                continue
            else:
                res.append(lst[i][4:lst[i].find('(')])
    if len(res) == 0:
        print('Best Programming Team')
    else:
        print('\n'.join(res))
