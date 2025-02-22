l = input().split()
mx = l[0]
mx2 = l[0]
for i in l:
    if i > mx:
        if mx2 < mx:
            mx2 = mx
        mx = i
print(mx2)