matriz = []
soma = 0
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

for l in range(4):
    for c in range(4):
        if l == c:
            soma += matriz[l][c]

print(soma)