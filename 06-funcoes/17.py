def distância(x, y):
    d = (((x ** 2) + (y ** 2)) ** (1 / 2))
    return d


# Programa principal
x = float(input(' Valor x: '))
y = float(input(' Valor y: '))
distancia = distância(x, y)
print(f'{distancia:.2f}')
