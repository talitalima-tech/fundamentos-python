def soma(x):
    soma = 0
    for numeros in range(1, x + 1):
        soma += numeros
    return soma

# Programa Principal
x = int(input(""))
soma = soma(x)
print(f"{soma}")