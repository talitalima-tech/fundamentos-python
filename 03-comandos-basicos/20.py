def triangulo_lateral(n):
    for i in range(1, n + 1):
        for i in range(i):
            print("*", end="")
        print("")
    for j in range(n - 1, 0, -1):
        for j in range(j):
            print("*", end= "")
        print("")

# Programa Principal
n = int(input())
triangulo_lateral(n)