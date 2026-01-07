def soma_pares(x):
    soma = 0
    for i in range(x):
        soma += 2 * i
    return soma

numero = int(input('Número: '))
soma = soma_pares(numero)
print(soma)






