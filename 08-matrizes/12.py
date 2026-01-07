matriz = []
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)
matriz2 = [[0] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        matriz2[i][j] = matriz[j][i]

for l in matriz2:
    for elemento in l:
        print(elemento, end=" ")
    print()

