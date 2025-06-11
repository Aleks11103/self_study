s = input()
d = {}
d_ans = {}
for el in s:
    d[el] = d.setdefault(el, 0) + 1
for _ in range(int(input())):
    lst = input().split(': ')
    d_ans[int(lst[1])] = lst[0]
ans = []
for el in s:
    ans.append(d_ans[d[el]])
print(''.join(ans))
