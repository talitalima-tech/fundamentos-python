matriz = []
soma = 0
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

for i in range(4):
    for j in range(4):
        if i > j:
            soma += matriz[i][j]

print(soma)