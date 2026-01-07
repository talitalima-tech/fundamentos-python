#E = 1 + 1/1! + 1/2! + 1/3! . . . 1/n!.
def funcao_E(x):
    fatorial = 1
    soma = 1
    for i in range(1, x + 1):
        fatorial *= 1 / i
        soma += fatorial
    return soma


# Programa Principal
x = int(input(""))
soma = funcao_E(x)
print(f"{soma:.8f}")