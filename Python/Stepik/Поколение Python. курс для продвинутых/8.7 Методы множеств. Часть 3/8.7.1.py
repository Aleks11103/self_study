set_1 = set([int(x) for x in input()])
set_2 = set([int(x) for x in input()])
if set_1.isdisjoint(set_2):
    print("NO")
else:
    print("YES")
