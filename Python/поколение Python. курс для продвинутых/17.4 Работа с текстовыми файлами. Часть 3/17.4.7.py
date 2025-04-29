with open('logfile.txt', 'r', encoding='utf-8') as f_in, \
        open('output.txt', 'w', encoding='utf-8') as f_out:
    for line in f_in:
        name, time_in, time_out = line.strip().split(', ')
        time_in = int(time_in[:2]) * 60 + int(time_in[3:])
        time_out = int(time_out[:2]) * 60 + int(time_out[3:])
        if time_out - time_in >= 60:
            f_out.write(f'{name}\n')
