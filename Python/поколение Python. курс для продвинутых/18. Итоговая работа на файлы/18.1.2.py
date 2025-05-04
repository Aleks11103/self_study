with open('ledger.txt', 'r', encoding='utf-8') as f:
    lst = [int(el[1:].strip()) for el in f]
    print(f'${sum(lst)}')
