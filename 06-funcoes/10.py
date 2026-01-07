def conversão_ângulo(g):
    r = g * (3.14159265359 / 180)
    return r


# Programa principal
graus = float(input('Ângulo em graus: '))
radiano = conversão_ângulo(graus)
print(f'{radiano:.2f}')