abscissas = [float(el) for el in input().split()]
ordinates = [float(el) for el in input().split()]
applicates = [float(el) for el in input().split()]
print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4,
              abscissas, ordinates, applicates)))
