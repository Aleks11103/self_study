a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
else:
    if a != 0:
        x = (c * c - b) / a
        xr = int(x)
        if (a * x + b) < 0:
            print('NO SOLUTION')
        elif xr == x:
            print(xr)
        else:
            print('NO SOLUTION')
    elif b == c * c:
        print('MANY SOLUTIONS')
    else: 
        print('NO SOLUTION')