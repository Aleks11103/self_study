with open('grades.txt', 'r', encoding='utf-8') as f:
    res = 0
    for line in f:
        lst = list(map(int, line.strip().split()[1:]))
        if lst[0] >= 65 and lst[1] >= 65 and lst[2] >= 65:
            res += 1
    print(res)
