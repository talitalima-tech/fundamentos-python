matriz_a = []
for l in range(5):
    linha = []
    for c in range(5):
        n = int(input())
        linha.append(n)
    matriz_a.append(linha)

matriz_b = []
for l in range(5):
    linha = []
    for c in range(5):
        num = int(input())
        linha.append(num)
    matriz_b.append(linha)

matriz_c = [[0 for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        for k in range(5):
            matriz_c[i][j] = matriz_c[i][j] + (matriz_a[i][k] * matriz_b[k][j])

for linha in matriz_c:
    for elem in linha:
        print(elem, end=" ")
    print()