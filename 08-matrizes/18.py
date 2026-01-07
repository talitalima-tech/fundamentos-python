import random

semente = int(input())
random.seed(semente)
linha = 5
coluna = 5
matriz = [[random.randint(1, 20) for i in range(coluna)] for j in range(linha)]

matriz2 = [[0] * 5 for i in range(linha)]
matriz2 = [[matriz[i][j] * (j <= i) for j in range(coluna)] for i in range(linha)]

for linha in matriz:
    for n in linha:
        print(n, end=" ")
    print()

print()

for linha in matriz2:
    for n in linha:
        print(n, end=" ")
    print()
