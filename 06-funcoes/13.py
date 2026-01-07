def valor_ganho(num):
    p1 = num * 0.46
    p2 = num * 0.32
    p3 = num * 0.22
    return p1, p2, p3


# Programa principal
valor = float(input('Valor: '))
p1, p2, p3 = valor_ganho(valor)
print(f'{p1:.2f}')
print(f'{p2:.2f}')
print(f'{p3:.2f}')