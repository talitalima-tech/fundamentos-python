matriz = []
for l in range(0, 5):
    linha = []
    for c in range(0, 5):
        num = int(input())
        linha.append(num)
    matriz.append(linha)

vetor = []
for l in range(5):
    soma = 0
    for c in range(5):
        soma += matriz[c][l]
    vetor.append(soma)

print(vetor)