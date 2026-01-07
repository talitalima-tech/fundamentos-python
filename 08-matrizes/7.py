matriz = []
for i in range(0, 10):
    linha = []
    for j in range(0, 10):
        if i < j:
            linha.append((2 * i) + (7 * j) - 2)
        if i == j:
            linha.append(3 * (i ** 2) - 1)
        if i > j:
            linha.append((4 * (i ** 3)) - (5 * (j ** 2)) + 1)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()