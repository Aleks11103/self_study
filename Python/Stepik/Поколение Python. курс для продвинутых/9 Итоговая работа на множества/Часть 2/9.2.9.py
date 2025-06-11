s1 = {el for el in input().split()}
s2 = {el for el in input().split()}
print(*sorted(s1 | s2))
