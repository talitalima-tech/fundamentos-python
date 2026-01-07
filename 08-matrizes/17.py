import math
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


matriz = []
for l in range(12):
    linha = []
    for c in range(13):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

matriz2 = []
for j in range(13):
    coluna = [matriz[i][j] for i in range(12)]

    primos = [n for n in coluna if eh_primo(n)]

    if primos:
        maior = max(primos)
        coluna_modificada = [n / maior for n in coluna]
    else:
        menor = min(coluna)
        coluna_modificada = [n / menor for n in coluna]

    matriz2.append(coluna_modificada)

matriz2 = list(zip(*matriz2))

for linha in matriz:
    for n in linha:
        print(f"{n:.2f}", end=" ")
    print()

print()

for linha in matriz2:
    for e in linha:
        print(f"{e:.2f}", end=" ")
    print()
