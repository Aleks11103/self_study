x1, y1, x2, y2 = map(int, input().split())

r1 = x1 + x2
r2 = y1 + x2
r3 = y1 + y2
r4 = x1 + y2

s1 = r1 * max(y1, y2)
s2 = r2 * max(x1, y2)
s3 = r3 * max(x1, x2)
s4 = r4 * max(y1, x2)
smin = min(s1, s2, s3, s4)

if s1 <= smin:
    print(r1, max(y1, y2))
elif s2 <= smin:
    print(r2, max(x1, y2))
elif s3 <= smin:
    print(r3, max(x1, x2))
else:
    print(r4, max(y1, x2))