lst = [int(x) for x in input().split()]
set_num = set()
for el in lst:
    if el in set_num:
        print("YES")
    else:
        print("NO")
        set_num.add(el)
