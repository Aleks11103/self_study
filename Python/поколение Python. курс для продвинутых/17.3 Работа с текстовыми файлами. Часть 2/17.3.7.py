from random import choice


with open('first_names.txt', 'r', encoding='utf-8') as f_names, \
        open('last_names.txt', 'r', encoding='utf-8') as f_surnames:
    names = [el.strip() for el in f_names.readlines()]
    surnames = [el.strip() for el in f_surnames.readlines()]
    for _ in range(3):
        print(f'{choice(names)} {choice(surnames)}')
