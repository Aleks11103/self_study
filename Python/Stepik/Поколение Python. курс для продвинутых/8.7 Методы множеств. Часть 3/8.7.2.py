set_1 = set([int(x) for x in input()])
set_2 = set([int(x) for x in input()])
if set_1.issuperset(set_2):
    print("YES")
else:
    print("NO")
