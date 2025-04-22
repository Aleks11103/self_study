name = input()
f = open(name, encoding='UTF8')
print(f.readlines()[-1])
f.close()
