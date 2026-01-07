matriz = []
soma = 0
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            while i >= 1:
                i -= 1
                soma += matriz[i][j]

print(soma)