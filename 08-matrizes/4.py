matriz = []
for l in range(0, 4):
    matriz.append([])
    for c in range(0, 4):
        num = int(input())
        matriz[l].append(num)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for l in range(4):
    for c in range(4):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            linha_maior = l
            coluna_maior = c
print(linha_maior)
print(coluna_maior)
print(maior)

