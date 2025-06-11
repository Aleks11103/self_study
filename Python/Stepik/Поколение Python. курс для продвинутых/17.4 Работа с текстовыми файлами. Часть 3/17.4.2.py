from random import randint


with open('random.txt', 'w', encoding='utf-8') as f_out:
    for _ in range(25):
        f_out.write(f'{randint(111, 777)}\n')
