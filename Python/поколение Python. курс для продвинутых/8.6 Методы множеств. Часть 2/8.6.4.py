n = int(input())
set_1 = set([int(x) for x in input()])
for _ in range(1, n):
    new_s = set([int(x) for x in input()])
    set_1.intersection_update(new_s)
print(*set_1)
