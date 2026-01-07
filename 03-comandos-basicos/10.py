def potencia(x, n):
    potencia = 1
    for i in range(n):
        potencia *= x
    return potencia

#Programa Principal
x = int(input())
n = int(input())
potencia = potencia(x, n)
print(f'{potencia}')
