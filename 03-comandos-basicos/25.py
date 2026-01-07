def funcao(n):
    soma = 0
    for i in range(1, n + 1):
        numerador = i ** 2 + 1
        denominador = i + 3
        fraçao = numerador / denominador
        soma += fraçao
    return soma

# Programa Principal
n = int(input())
soma = funcao(n)
print(f'{soma:.2f}')