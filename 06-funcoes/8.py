def conversão_temperatura(num):
    f = num * 9 / 5 + 32
    return f


# Programa principal
celsius = float(input('Temperatura em Celsius: '))
c = conversão_temperatura(celsius)
print(f'{c:.2f}')