import random


tickets = set()
while len(tickets) < 100:
    res = [str(random.randint(1, 9))]
    for _ in range(6):
        res.append(str(random.randint(0, 9)))
    tickets.add(''.join(res))
for el in tickets:
    print(el)
