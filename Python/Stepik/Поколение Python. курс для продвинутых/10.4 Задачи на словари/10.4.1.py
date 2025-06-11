n = int(input())
d = {}
for _ in range(n):
    key, value = input().split(': ')
    d[key.lower()] = value
for _ in range(int(input())):
    s = input().lower()
    if s in d:
        print(d[s])
    else:
        print('Не найдено')
