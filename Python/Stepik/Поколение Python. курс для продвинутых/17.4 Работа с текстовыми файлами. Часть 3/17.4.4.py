with open('class_scores.txt', 'r', encoding='utf-8') as f_out, \
        open('new_scores.txt', 'w', encoding='utf-8') as f_in:
    for line in f_out:
        name, score = line.strip().split()
        score = int(score)
        if score <= 95:
            f_in.write(f'{name} {score + 5}\n')
        else:
            f_in.write(f'{name} 100\n')
