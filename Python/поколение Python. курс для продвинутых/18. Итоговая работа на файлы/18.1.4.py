with open('words.txt', 'r', encoding='utf-8') as f:
    lst = f.read().split()
    max_len = len(max(lst, key=lambda x: len(x)))
    print(*filter(lambda x: len(x) == max_len, lst), sep='\n')
