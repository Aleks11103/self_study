def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as f:
        res = []
        names = f.readline().strip().split(',')
        for line in f:
            d = {}
            for i, el in enumerate(line.strip().split(',')):
                d[names[i]] = el
            res.append(d)
    return res


print(read_csv())
