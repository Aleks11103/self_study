with open(input(), 'r', encoding='utf-8') as f_in, \
        open('forbidden_words.txt', 'r', encoding='utf-8') as f_block:
    s = f_in.read()
    lst_change = f_block.read().split()
    for el in lst_change:
        while (pos := s.lower().find(el)) >= 0:
            s = s[:pos] + '*' * len(el) + s[pos+len(el):]
    print(s)
