from string import ascii_lowercase as low, ascii_uppercase as upp, digits


s = input()
print('YES' if all((len(s) >= 7,
                    any(map(lambda x: x in low, s)),
                    any(map(lambda x: x in upp, s)),
                    any(map(lambda x: x in digits, s))
                    ))
      else 'NO')
