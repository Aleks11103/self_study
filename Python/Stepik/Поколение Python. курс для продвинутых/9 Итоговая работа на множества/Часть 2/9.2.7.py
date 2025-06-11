m = int(input())
n = int(input())
s_math = set()
s_inform = set()
for _ in range(m):
    s_math.add(input())
for _ in range(n):
    s_inform.add(input())
print(len(s_math - s_inform))
