with open('data.txt', 'r', encoding='utf-8') as f:
    print(*f.readlines()[-1::-1], sep='')
