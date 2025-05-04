with open('file.txt', 'r', encoding='utf-8') as f:
    counter = [0, 0, 0]  # letters, words, lines
    for line in f:
        counter[2] += 1
        words = [el.strip(' \n\t,.:;-\'"!?') for el in line.split()]
        counter[1] += len(words)
        for word in words:
            for el in word:
                if el.isalpha():
                    counter[0] += 1
    print(f"""Input file contains:
{counter[0]} letters
{counter[1]} words
{counter[2]} lines""")
