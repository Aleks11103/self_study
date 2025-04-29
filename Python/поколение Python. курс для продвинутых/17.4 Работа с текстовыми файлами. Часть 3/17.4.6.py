with open('output.txt', 'a', encoding='utf-8') as f_out:
    for _ in range(int(input())):
        f = open(input(), 'r', encoding='utf-8')
        f_out.write(f.read())
        f.close()
