# Кэширование запросов

n, m = map(int, input().split())
d = {}

for i in range(1, n + 1):
    s, t = input().split()
    t = int(t)
    if s in d:
        if d[s] < t:
            print(i, 'UPDATE', s)
            d[s] = t
    else:
        if len(d) < m:
            d[s] = t
            print(i, 'PUT', s)
        else:
            min_val = min(d.values())
            if min_val < t:
                for key, value in d.items():
                    if value == min_val:
                        print(i, 'DELETE', key)
                        del_key = key
                        break
                del d[del_key]
                d[s] = t
                print(i, 'PUT', s)