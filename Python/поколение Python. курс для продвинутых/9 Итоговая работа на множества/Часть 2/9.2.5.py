num_1 = {int(x) for x in input().split()}
num_2 = {int(x) for x in input().split()}
res_num = num_1.intersection(num_2)
if len(res_num) > 0:
    print(*sorted(res_num, reverse=True))
else:
    print("BAD DAY")
