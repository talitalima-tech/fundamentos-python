matriz = []
for l in range(0, 5):
    matriz.append([])
    for c in range(0, 5):
        num = int(input())
        matriz[l].append(num)

n = int(input())

encontrado = False
for l in range(5):
    for c in range(5):
        if matriz[l][c] == n:
            print(f"{l}")
            print(f"{c}")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("Nao encontrado")
