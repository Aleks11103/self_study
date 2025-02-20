# Напишите функцию func, которая проверит ваш пароль на сложность. Функция
# принимает в себя пароль(строку), в пароле в обязательном порядке должны
# присутствовать:
# - не менее 1ой цифры
# - не менее 1ой буквы в нижнем и верхнем регистре
# - хотя бы 1 символ из строки "!@#$%*"
# - общее количество символов не менее 8ми.
# Если функция не проходит любую из проверок - выводится
# "Плохо. Но я уверен ты сможешь! Наверное...".
# Если все проверки пройдены вывести - "Шикарный пароль!"
# Функцию вызывать не нужно.

def func(s):
    if len(s) < 8:
        print("Плохо. Но я уверен ты сможешь! Наверное...")
    else:
        f_num = False
        f_low = False
        f_up = False
        f_sym = False
        for el in s:
            if not f_num and el.isdigit():
                f_num = True
            elif not f_low and el in "abcdefghijklmnopqrstuvwxyz":
                f_low = True
            elif not f_up and el in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                f_up = True
            elif not f_sym and el in "!@#$%*":
                f_sym = True
        if f_num and f_low and f_up and f_sym:
            print("Шикарный пароль!")
        else:
            print("Плохо. Но я уверен ты сможешь! Наверное...")


s = input()
func(s)
