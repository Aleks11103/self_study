d = {}
for _ in range(int(input())):
    s1, s2 = input().split()
    d[s1] = s2
    d[s2] = s1
print(d[input()])
