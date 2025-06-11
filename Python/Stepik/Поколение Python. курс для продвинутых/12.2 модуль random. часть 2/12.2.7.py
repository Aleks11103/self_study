n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
for i in range(n):
    print(f"{lst[i]} - {lst[i - 1]}")
