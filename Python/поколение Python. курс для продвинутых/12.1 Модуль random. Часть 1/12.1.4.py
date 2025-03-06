import random


res = set()
while len(res) < 7:
    res.add(random.randint(1, 49))
print(*sorted(res))
