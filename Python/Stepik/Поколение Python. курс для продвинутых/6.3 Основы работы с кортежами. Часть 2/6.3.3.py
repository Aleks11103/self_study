poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
lst_data = list(poet_data)
lst_data[2] = 'Москва'
poet_data = tuple(lst_data)
print(poet_data)
