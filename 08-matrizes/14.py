matriz_a = []
for l in range(4):
    linha = []
    for c in range(5):
        n = int(input())
        linha.append(n)
    matriz_a.append(linha)

matriz_b = []
for l in range(4):
    linha = []
    for c in range(5):
        num = int(input())
        linha.append(num)
    matriz_b.append(linha)

matriz_c = []
for i in range(len(matriz_a)):
    linha = []
    for j in range(len(matriz_a[0])):
        n = matriz_a[i][j] + matriz_b[i][j]
        linha.append(n)
    matriz_c.append(linha)

for linha in matriz_c:
    for elem in linha:
        print(elem, end=" ")
    print()
