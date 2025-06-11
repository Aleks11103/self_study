n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())
b = n + m - t - x
c = m + k - t - y
d = n + k - t - z
print(n + m + k - 2 * (b + d + c) - 3 * t)
print(b + d + c)
print(a - d - b - c - t - (n - b - d - t) - (m - b - t - c) - (k - d - t - c))
