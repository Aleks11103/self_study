f = open('prices.txt', encoding='UTF8')
res = 0
for line in f.readlines():
    count, cost = map(int, line.split('\t')[1:])
    res += count * cost
print(res)
