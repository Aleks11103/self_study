# На соревнованиях по бегу должно быть 3 забега, в каждом последующем забеге
# не должны участвовать спортсмены из предыдущих. Т.е. вам необходимо исключить
# спортсменов, пытающихся повторно участвовать
# в забегах. Дан кортеж множеств, каждое множество - это коллекция имен
# участников забега. Необходимо только изменить кортеж множеств, на экран
# не выводить.

# вводные данные
athletes = (
            {'Дамблдор', 'Егор', 'Максим', 'Конь', 'Владимир', 'Никита',
             'Ринат'},
            {'Флеш', 'Вадим', 'Никита', 'Николай', 'Дипси', 'Олег',
             'Александр'},
            {'Вучич', 'Егор', 'Николай', 'Конь', 'Дмитрий', 'Шишига',
             'Тимофей', 'Артем'}
)

# продолжите решение здесь
athletes[1].difference_update(athletes[0])
athletes[2].difference_update(athletes[0])
athletes[2].difference_update(athletes[1])
print(athletes)
