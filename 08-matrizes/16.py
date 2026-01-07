matriz = []
for l in range(12):
    linha = []
    for c in range(13):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

matriz2 = []
for linha in matriz:
    maior = max(abs(num) for num in linha)
    if maior == 0:
        matriz2.append(linha)
    else:
        matriz2.append([num / maior for num in linha])

for linha in matriz:
    for n in linha:
        print(f"{n:.2f}", end=" ")
    print()

print()

for linha in matriz2:
    for e in linha:
        print(f"{e:.2f}", end=" ")
    print()

