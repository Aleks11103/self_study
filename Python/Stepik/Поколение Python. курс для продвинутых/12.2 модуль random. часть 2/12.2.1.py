import random


res = []
for _ in range(4):
    res.append(str(random.randint(1, 255)))
print('.'.join(res))
