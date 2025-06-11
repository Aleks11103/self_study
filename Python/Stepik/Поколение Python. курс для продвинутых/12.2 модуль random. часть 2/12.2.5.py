import random


word = input()
lst = list(word)
random.shuffle(lst)
print(''.join(lst))
