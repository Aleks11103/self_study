# В Тульской области рухнуло НЛО, зацепившись за ветку сосны. На месте крушения
# были найдены доказательства слежки за людьми. Вам дана одна из анкет в
# найденном архиве на случайного человека. Анкета представляет собой словарь,
# который вам дан. На вход поступают слова через пробел в одну строку, если они
# являются ключами этого словаря, то их необходимо добавить в новый словарь с
# соответствующими значениями, иначе игнорировать.

# вводные данные 
user = {
    "id": 1,
    "имя": "Моисей",
    "фамилия": "Борисов",
    "username": "supermos'ka43",
    "email": "moisbor43@mail.com",
    "пол": "неопределён",
    "адрес": "Москва, ул. Тазобедренная 47",
    "номер_телефона": "+84575938657",
    "дата_рождения": "1936-09-17",
    "работа": {
        "название_организации": "МосГорВодПотКотРотКротГазВотТеРаз ",
        "должность": "дождевик"
    },
}

# продолжить решение здесь
print({s: user[s] for s in input().split() if s in user})
