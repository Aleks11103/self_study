# Арсений учится делать ботов. Он написал простого "зеркального" бота, который
# отвечает тем же сообщением, что написали ему. Но похоже этот бот начал
# проявлять признаки интеллекта и иногда отвечает другими словами(иногда
# обидными). На вход подается строка, затем еще одна, если они равны вывести
# "полное соответствие", иначе "сбой бота".

print("полное соответствие" if input() == input() else "сбой бота")
