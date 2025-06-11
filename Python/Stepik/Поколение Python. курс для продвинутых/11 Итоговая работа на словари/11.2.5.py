def merge(values):      # values - это список словарей
    d = {}
    for el in values:
        for key in el:
            d.setdefault(key, set()).add(el[key])
    return d


print(merge([{'a': 1, 'b': 2},
             {'b': 10, 'c': 100},
             {'a': 1, 'b': 17, 'c': 50},
             {'a': 5, 'd': 777}]))
