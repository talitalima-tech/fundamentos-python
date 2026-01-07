def quadrado(num):
    q = num ** 2
    return q


# Programa principal
numero = float(input('número: '))
quadrado = quadrado(numero)
print(f'{quadrado:.2f}')