with open('population.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, count = line.strip().split('\t')
        if name[0] == 'G' and int(count) > 500_000:
            print(name)
