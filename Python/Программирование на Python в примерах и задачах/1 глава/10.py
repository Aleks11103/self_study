l = [int(i) for i in input().split()]
s = 0
for i in l:
    if s % 2 == 1:
        s += i
print(s)