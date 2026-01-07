def numero_harmonico(n):
    soma_numeros = 0
    for i in range(1, n + 1):
        soma_numeros += 1 / i
    return soma_numeros


# Program Principal
n = int(input())
soma = numero_harmonico(n)
print(f"{soma:.2f}")