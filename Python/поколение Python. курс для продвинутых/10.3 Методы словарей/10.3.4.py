s = 'orange strawberry barley gooseberry apple apricot barley currant orange\
     melon pomegranate banana banana orange barley apricot plum grapefruit\
     banana quince strawberry barley grapefruit banana grapes melon strawberry\
     apricot currant currant gooseberry raspberry apricot currant orange lime\
     quince grapefruit barley banana melon pomegranate barley banana orange\
     barley apricot plum banana quince lime grapefruit strawberry gooseberry\
     apple barley apricot currant orange melon pomegranate banana banana\
     orange apricot barley plum banana grapefruit banana quince currant orange\
     melon pomegranate barley plum banana quince barley lime grapefruit\
     pomegranate barley'
res = {}
for el in s.split():
    res[el] = res.get(el, 0) + 1
max_val = max(res.values())
res_lst = []
for key, value in res.items():
    if value == max_val:
        res_lst.append(key)
print(min(res_lst))
