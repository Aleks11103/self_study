d = {}
for _ in range(int(input())):
    name, tov, count = input().split()
    count = int(count)
    if name in d:
        if tov in d[name]:
            d[name][tov] += count
        else:
            d[name][tov] = count
    else:
        d[name] = {tov: count}
for name in sorted(d.keys()):
    print(f"{name}:")
    for key in sorted(d[name].keys()):
        print(key, d[name][key])
