import random
from string import ascii_uppercase

lst = []
for _ in range(4):
    lst.append(random.choice(ascii_uppercase))
res = []
res.append(lst[0] + lst[1] + str(random.randint(0, 99)))
res.append(str(random.randint(0, 99)) + lst[2] + lst[3])
print('_'.join(res))
