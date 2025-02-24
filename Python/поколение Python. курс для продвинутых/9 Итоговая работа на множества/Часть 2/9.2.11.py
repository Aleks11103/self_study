m = int(input())
n = int(input())
all_set = {input() for _ in range(n)}
for _ in range(1, m):
    n = int(input())
    students = {input() for _ in range(n)}
    all_set &= students
for el in sorted(all_set):
    print(el)
