lst = input().lower().split()
set_words = set()
for word in lst:
    set_words.add(word.strip(".,;:-?!"))
print(len(set_words))
