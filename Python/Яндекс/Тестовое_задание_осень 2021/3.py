# Мониторинг логов
import time

flag = False
with open('input.txt', 'r') as f:
    s = f.readline()
    K, e = map(int, s.split())
    time_list = []
    for s in f:
        s_time = s[1:20]
        s_status = s[22:s.find(' ', 22)]
        if s_status == 'ERROR':
            t = time.mktime(time.strptime(s_time, '%Y-%m-%d %H:%M:%S'))
            while len(time_list) > 0 and t - time_list[0] + 1 > K:
                time_list.pop(0)
            time_list.append(t)
            if len(time_list) >= e:
                t = t + 3600 * 3
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t)))
                flag = True
                break
if flag == False:
    print(-1)


# K, e = map(int, input().split())

# time_list = []

# s = input()
# while s != '\n':
    
#     s_time = s[1:20]
#     s_status = s[22:s.find(' ', 22)]
#     if s_status == 'ERROR':
#         t = time.mktime(time.strptime(s_time, '%Y-%m-%d %H:%M:%S'))
#         while len(time_list) > 0 and t - time_list[0] + 1 > K:
#             time_list.pop(0)
#         time_list.append(t)
#         if len(time_list) >= e:
#             print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t)))
#     s = input()
# else:
#     print(-1)