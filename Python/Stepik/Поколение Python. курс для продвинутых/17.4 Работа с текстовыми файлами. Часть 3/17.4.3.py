with open('input.txt', 'r', encoding='utf-8') as f, \
        open('output.txt', 'w', encoding='utf-8') as f_out:
    for i, line in enumerate(f):
        f_out.write(f'{i+1}) {line}')
