n = int(input())
numero = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        numero += 1
        print(numero, end=" ")
    print("")

n = int(input())
triangulo_floyd(n)