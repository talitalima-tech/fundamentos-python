matriz = []
num = int(input())
for l in range(num):
    matriz.append([0] * num)

for l in range(num):
    matriz[l][l] = 1

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
