def área(lado):
    a = lado ** 2
    return a


# Programa principal
lado = float(input('lado: '))
area = área(lado)
print(f'{area:.2f}')
