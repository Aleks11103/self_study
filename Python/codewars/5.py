# Добро пожаловать.

# В этом ката от вас требуется, получив строку, заменить каждую букву на ее позицию в алфавите.

# Если что-то в тексте не является буквой, проигнорируйте это и не возвращайте.

# "a" = 1, "b" = 2 и т.д.


def alphabet_position(text):
    res = []
    for i in text:
        if (ord(i) >= 65 and ord(i) <= 90):
            res.append(str(ord(i) - 64))
        elif (ord(i) >= 97 and ord(i) <= 122):
            res.append(str(ord(i) - 96))
    return " ".join(res).strip()


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))