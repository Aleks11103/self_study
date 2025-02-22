t_room, t_cond = map(int, input().split())
mode = input()

if mode == 'freeze':
    if t_room <= t_cond:
        print(t_room)
    else:
        print(t_cond)
elif mode == 'heat':
    if t_room >= t_cond:
        print(t_room)
    else:
        print(t_cond)
elif mode == 'auto':
    print(t_cond)
elif mode == 'fan':
    print(t_room)