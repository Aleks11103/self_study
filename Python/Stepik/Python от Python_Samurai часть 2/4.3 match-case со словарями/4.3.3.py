# Дан объемный кортеж tpl со вложенными данными. Необходимо на основе него
# создать список lst со вложенными
# списками, пример вложенного списка:

# ['name: Список Шиндлера', 'year: 1993', 'genre: драма, фэнтези, криминал',
# 'director: Стивен Спилберг', 'rating: 8.8']

# Соответственно список lst будет формироваться при переборе кортежа tpl.
# В итоговый список попадут только списки и словари(которые нужно преобразовать
# в списки по принципу примера выше) из кортежа tpl, которые будут
# соответствовать необходимым шаблонам.  Длина входящего списка должна быть не
# менее 4ех. Также в списке, обязательно наличие элементов, содержащих в себе
# подстроку  'name' и 'rating'. Если это словарь, то обязательно наличие ключей
# 'name' и 'rating', количество ключей не менее 4ёх. Во всех случаях рейтинг
# должен быть более 8.6. Кортежи на входе игнорируются. Внутри формирующихся
# списков должны быть объекты строки разделенные ": ", если на вход зашел
# список, в котором внутри строк есть ' - ' данное разделение надо исправить.
# Полученный список вывести командой print(*lst, sep='\n').


# исходные данные
tpl = (
    ('name: Зелёная миля', 'year: 1999', 'genre: драма, фэнтези, криминал',
     'director: Фрэнк Дарабонт', 'rating: 9.1'),
    ['name: Список Шиндлера', 'year: 1993', 'genre: драма, фэнтези, криминал',
     'director: Стивен Спилберг', 'rating: 8.8'],
    ['name - Побег из Шоушенка', 'year - 1994', 'genre - драма',
     'director - Фрэнк Дарабонт', 'rating - 9.1'],
    {'name': 'Форрест Гамп', 'year': '1994',
     'genre': 'драма, комедия, мелодрама, история, военный',
     'director': 'Роберт Земекис', 'rating': '8.9'},
    ('name: Тайна Коко', 'year: 2017',
     'genre: мультфильм, фэнтези, комедия, приключения, семейный',
     'director: Ли Анкрич', 'rating: 8.7'),
    ['name: Властелин колец: Возвращение короля', 'year: 2003',
     'genre: фэнтези, приключения, драма, боевик',
     'director: Питер Джексон', 'rating: 8.7'],
    {'name': 'Интерстеллар', 'year': '2014',
     'genre': 'фантастика, драма, приключения',
     'director': 'Кристофер Нолан', 'rating': '8.6'},
    ['name - Криминальное чтиво', 'year - 1994', 'genre - криминал, драма',
     'director - Квентин Тарантино', 'rating - 8.6'],
    ['name: Бойцовский клуб', 'director: Дэвид Финчер', 'rating: 8.7'],
    ['name - Властелин колец: Братство Кольца', 'year - 2001',
     'genre - фэнтези, приключения, драма, боевик',
     'director - Питер Джексон', 'rating - 8.6'],
    ['name: Назад в будущее', 'year: 1985',
     'genre: фантастика, комедия, приключения',
     'director: Роберт Земекис'],
    {'name': 'Властелин колец: Две крепости', 'year': '2002',
     'genre': 'фэнтези, приключения, драма, боевик',
     'director': 'Питер Джексон', 'rating': '8.6'},
    ('name: Иван Васильевич меняет профессию', 'year: 1973',
     'genre: комедия, фантастика, приключения',
     'director: Леонид Гайдай', 'rating: 8.8'),
    ['year: 1994', 'genre: мультфильм, мюзикл, драма, приключения, семейный',
     'director: Роджер Аллерс', 'rating: 8.8'],
    ['name: Черная роза', 'year: 2014', 'genre: шлак',
     'director: Александр Невский', 'rating: 1.5'],
    ['name - Судный день: Носик в сметанке', 'year - 1999',
     'genre - драма, фэнтези, кулинария, катастрофа',
     'director - Альфред Стилкок', 'rating - 9.1']
)

# продолжите решение здесь
lst = []
for el in tpl:
    match el:
        case [name, year, genre, director, rating] if isinstance(el, list) and float(rating[-3:]) > 8.6:
            res = []
            if 'name: ' in name:
                s_name = 'name: ' + name[6:]
            else:
                s_name = 'name: ' + name[7:]
            res.append(s_name)
            if 'year: ' in year:
                s_year = 'year: ' + year[6:]
            else:
                s_year = 'year: ' + year[7:]
            res.append(s_year)
            if 'genre: ' in genre:
                s_genre = 'genre: ' + genre[7:]
            else:
                s_genre = 'genre: ' + genre[8:]
            res.append(s_genre)
            if 'director: ' in director:
                s_director = 'director: ' + director[10:]
            else:
                s_director = 'director: ' + director[11:]
            res.append(s_director)
            if 'rating: ' in rating:
                s_rating = 'rating: ' + rating[8:]
            else:
                s_rating = 'rating: ' + rating[9:]
            res.append(s_rating)
            lst.append(res)
            # print(el)
        case {'name': name, 'year': year, 'genre': genre, 'director': director, 'rating': rating} if float(rating) > 8.6:
            res = []
            res.append('name: ' + name)
            res.append('year: ' + year)
            res.append('genre: ' + genre)
            res.append('director: ' + director)
            res.append('rating: ' + rating)
            lst.append(res)
            # print(el)
print(*lst, sep='\n')
