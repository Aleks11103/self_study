# У Рината свидание(наконец-то). К нему домой на романтический ужин должна
# прийти девушка(надеюсь). Проблема в том, что времени осталось мало и он
# по-быстрому в шкаф для одежды закинул различные вещи, чтобы дома был порядок.
# Естественно Ринат, потом решил вытащить из шкафа лишнее, оставив только самое
# необходимое. Вам дано множество(шкаф) где хранятся объекты(вещи). Так же на
# вход подается список слов(вещей) в одну строку через пробел. Нужно удалить
# элементы списка из множества. Преобразовать итоговое множество в
# отсортированный список и вывести элементы в консоль
# в одну строку через пробел.
st = {'носки', 'бензопила', 'штаны', 'флаг_Гваделупы',
      'перчатки', 'футболки', 'бабушка', 'кофта',
      'арбалет', 'шапка', 'холодец'}
lst = input().split()
for el in lst:
    st.discard(el)
print(*sorted(st))
