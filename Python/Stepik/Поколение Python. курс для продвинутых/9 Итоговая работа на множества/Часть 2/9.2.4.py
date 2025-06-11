m = int(input())
n = int(input())
need_read = [input() for _ in range(m)]
have_books = [input() for _ in range(n)]
for el in have_books:
    print("YES") if el in need_read else print("NO")
