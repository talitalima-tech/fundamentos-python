matriz = []
for l in range(0, 4):
    matriz.append([])
    for c in range(0, 4):
        num = int(input())
        matriz[l].append(num)

cont = 0
for l in range(4):
    for c in range(4):
        if matriz[l][c] > 10:
            cont += 1

print(cont)