n = int(input())
chars = set()
for _ in range(n):
    s = input().lower()
    for el in s:
        chars.add(el)
print(len(chars))
