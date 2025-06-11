def gematr(s):
    res = 0
    code_A = ord('A')
    for el in s.upper():
        res += ord(el) - code_A
    return res


n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
print(*sorted(lst, key=(lambda x: (gematr(x), x))), sep='\n')
