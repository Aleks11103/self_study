with open(input(), 'r', encoding='utf-8') as f:
    print(*f.readlines()[-10:], sep='')
