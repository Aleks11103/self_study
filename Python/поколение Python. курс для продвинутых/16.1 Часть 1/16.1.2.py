def pretty_print(*args, side='-', delimiter='|'):
    s = f'{delimiter} ' + f' {delimiter} '.join(map(str, args[0])) +\
        f' {delimiter}'
    s_side = ' ' + side * (len(s) - 2) + ' '
    print(s_side, s, s_side, sep='\n')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
