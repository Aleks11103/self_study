import re

def getNumber(s):
    if len(s) == 7:
        n = '495' + s
    else:
        n = s[1:]
    return n

def checkNumber(n, n1):
    if n == n1:
        return 'YES'
    else:
        return 'NO'

s = re.sub('[^0-9]', '', input())
s1 = re.sub('[^0-9]', '', input())
s2 = re.sub('[^0-9]', '', input())
s3 = re.sub('[^0-9]', '', input())

print(checkNumber(getNumber(s), getNumber(s1)))
print(checkNumber(getNumber(s), getNumber(s2)))
print(checkNumber(getNumber(s), getNumber(s3)))