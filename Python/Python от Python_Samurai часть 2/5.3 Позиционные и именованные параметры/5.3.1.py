# Фрезеровщик Федор устал терять пальцы на работе(остался 1 и то на ноге).
# И подумал - классно было бы написать программу, которая будет управлять
# станком и запустит его через определенный промежуток времени, чтобы можно
# было уйти на безопасное расстояние. Нужно создать функцию func, которая имеет
# именованный параметр t равный 5. При запуске функции возвращается строка:

# Работа станка начнется через <t> секунд.
# Ожидание запуска...
# Работа начата.

def func(t=5):
    return f"Работа станка начнется через {t} секунд.\nОжидание запуска...\nРабота начата."


t = int(input("Введите время ожидания до начала работы: "))
print(func(t))
