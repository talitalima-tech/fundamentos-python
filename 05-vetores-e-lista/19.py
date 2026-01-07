def funcao(x1, x2):
    x3 = [None] * (2 * len(x1))

    # Preenche o vetor resultado
    for i in range(len(x1)):
        x3[2 * i] = x1[i]  # Posições pares
        x3[2 * i + 1] = x2[i]  # Posições ímpares

    return x3

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)