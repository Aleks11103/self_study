#Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке.
s = input('s: ')
a = s[:s.find('h') + 1]
b = s[s.rfind('h') - 1:s.find('h'):-1]
c = s[s.rfind('h'):]
print(a + b + c)