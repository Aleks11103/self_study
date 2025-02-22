import json

with open('input.txt', 'r') as f:
    s = ''
    for line in f:
        s += line.rstrip()

    l_order = []
    l = json.loads(s)
    for elem in l:
        if elem["status"] == "OK" and elem["count"] > 0 and elem["count"] - elem["return_count"] > 0:
            
            print(elem)
        