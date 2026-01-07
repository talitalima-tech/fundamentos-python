import random
matriz = []
m = int(input(""))
n = int(input(""))
semente = int(input(""))
random.seed(semente)
inicial = int(input(""))
final= int(input(""))

for i in range(m):
    linha = []
    for j in range(n):
        numeros = random.randint(inicial,final)
        linha.append(numeros)
    matriz.append(linha)

for i in range(m):
    for j in range(n):
        print(matriz[i][j], end = " ")
    print()

pares = 0
c = 0
c_impar = 0
for i in range(m):
    pares = 0
    c = 0
    c_impar = 0
    for j in range(n):
        if i % 2 == 0:
            pares += matriz[i][j]
            c += 1
        if i % 2 == 1 and matriz[i][j] < 0 and matriz[i][j] % 3 == 0:
            c_impar += 1
    if c != 0:
        print(f"{pares/c:.2f}")
    if i % 2 == 1:
        print(f"{c_impar}")