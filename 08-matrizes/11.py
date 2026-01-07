matriz = []
soma = 0
n = 4
for l in range(0, 4):
    linha = []
    for c in range(0, 4):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

for l in range(4):
    for c in range(4):
        if l + c == n - 1:
            soma += matriz[l][c]
print(soma)
