h1 = int(input('часы 1: '))
m1 = int(input('минуты 1: '))
s1 = int(input('секунды 1: '))
h2 = int(input('часы 2: '))
m2 = int(input('минуты 2: '))
s2 = int(input('секунды 2: '))

time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

print(time2 - time1)