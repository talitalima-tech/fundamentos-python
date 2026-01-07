def valor_recebido(a, b, c, d):
    total = a + b + c
    r1 = (a / total) * d
    r2 = (b / total) * d
    r3 = (c / total) * d
    return r1, r2, r3


# Programa principal
inv1 = float(input('Valor investido: '))
inv2 = float(input('Valor insvestido: '))
inv3 = float(input('Valor investido: '))
premio = float(input('Valor do prêmio: '))
r1, r2, r3 = valor_recebido(inv1, inv2, inv3, premio)
print(f'{r1:.2f}')
print(f'{r2:.2f}')
print(f'{r3:.2f}')