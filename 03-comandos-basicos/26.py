import math

def taylor_seno(x, n):
    seno = 0
    for i in range(n + 1):
        coeficiente = (-1) ** i
        numerador = x ** (2 * i + 1)
        denominador = math.factorial(2 * i + 1)
        resultado = coeficiente * (numerador / denominador)
        seno += resultado
    return seno


# Programa Principal
radiano = float(input(""))
numero = int(input(""))
seno_angulo = taylor_seno(radiano, numero)
print(f'{seno_angulo:.8f}')