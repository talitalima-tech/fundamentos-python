def altura_triangulo(n):
    l = 2 * n - 1
    for i in range(1, n + 1):
        linha = "*" * (2 * i - 1)
        y = linha.center(l, " ")
        print(y)


# Programa Principal
n = int(input())
resultado = altura_triangulo(n)
