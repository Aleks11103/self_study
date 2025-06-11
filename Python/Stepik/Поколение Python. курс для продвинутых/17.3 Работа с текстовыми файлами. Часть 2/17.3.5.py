res = 0
with open('nums.txt', 'r', encoding='utf-8') as f:
    lst = []
    for el in f.read():
        if el in '0123456789':
            lst.append(el)
        else:
            s_num = ''.join(lst)
            if s_num.isdigit():
                res += int(s_num)
            lst.clear()
print(res)
