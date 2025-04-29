with open('goats.txt', 'r', encoding='utf-8') as f_out, \
        open('answer.txt', 'w', encoding='utf-8') as f_in:
    d = {}
    f_out.readline()
    counter = 1
    while (line := f_out.readline().strip()) != 'GOATS':
        d[line] = 0
    f_out.readline()
    for line in f_out:
        d[line.strip()] += 1
        counter += 1
    for key, value in sorted(d.items()):
        if value > int(counter * 0.07):
            f_in.write(f'{key}\n')
