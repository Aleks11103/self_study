with open('lines.txt') as f:
    lst = [el.strip() for el in f.readlines()]
    max_len = len(max(lst, key=lambda x: len(x)))
    print(*filter(lambda x: len(x) == max_len, lst), sep='\n')
