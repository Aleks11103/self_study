with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        res = 0
        lst = map(int, line.split())
        res += sum(lst)
        print(res)
