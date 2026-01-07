def conversão_velocidade(k):
    m = k / 3.6
    return m


# Programa principal
km = float(input('Velocidade em km/h: '))
metro = conversão_velocidade(km)
print(f'{metro:.2f}')