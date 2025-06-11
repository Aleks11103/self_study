n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
if input() in lst:
    print("REPEAT")
else:
    print("OK")
