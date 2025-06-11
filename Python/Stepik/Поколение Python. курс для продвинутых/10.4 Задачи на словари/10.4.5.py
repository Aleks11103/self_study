d = {}
for _ in range(int(input())):
    lst = input().split()
    d[lst[0]] = lst[1:]
for _ in range(int(input())):
    city = input()
    for key, value in d.items():
        if city in value:
            print(key)
            break
