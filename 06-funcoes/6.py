# Volume e área de esfera
def volume(raio):
    v = (4 / 3) * 3.14159265359 * (raio ** 3)
    return v

def área(raio):
    a = 4 * 3.14159265359 * (raio ** 2)
    return a


# Programa principal
raio = float(input('raio: '))
volume = volume(raio)
area = área(raio)
print(f'{volume:.2f}')
print(f'{area:.2f}')

