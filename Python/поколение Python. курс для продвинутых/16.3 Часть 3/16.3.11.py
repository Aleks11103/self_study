def int_ip(s):
    a, b, c, d = map(int, s.split('.'))
    return a * 256**3 + b * 256**2 + c * 256 + d


n = int(input())
lst = [input() for _ in range(n)]
print(*sorted(lst, key=lambda x: int_ip(x)), sep='\n')
