with open('text.txt', 'r', encoding='UTF8') as f:
    print(f.read()[-1::-1])
