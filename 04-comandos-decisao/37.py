def mdc(x1, x2):
    while x2:
        x1, x2 = x2, x1 % x2
    return x1


def simplificada(x1, x2):
    if x1 == 0:
        return (0, 1)

    mdc_valor = mdc(x1, x2)
    numerador_simplificado = x1 // mdc_valor
    denominador_simplificado = x2 // mdc_valor

    if denominador_simplificado < 0:
        numerador_simplificado = -numerador_simplificado
        denominador_simplificado = -denominador_simplificado

    return (numerador_simplificado, denominador_simplificado)

x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificada(x1, x2)
print(f"{y1}")
print(f"{y2}")