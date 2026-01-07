matriz = []
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

matriz_2 = []
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        n = int(input())
        linha.append(n)
    matriz_2.append(linha)

matriz_3 = [[0] * 4 for _ in range(4)]

for l in range(4):
    for c in range(4):
        if matriz[l][c] > matriz_2[l][c]:
            matriz_3[l][c] = matriz[l][c]
        else:
            matriz_3[l][c] = matriz_2[l][c]

for linha in matriz_3:
    for elemento in linha:
        print(elemento, end=" ")
    print()