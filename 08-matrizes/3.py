matriz = []
num = int(input())
for l in range(num):
    linha = []
    for c in range(num):
        linha.append(l * c)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
