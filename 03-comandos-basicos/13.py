def fibonacci(n):
    f1 = 1
    f2 = 1
    fn = 1

    for i in range(n - 2):
        fn = f1 + f2
        f1 = f2 #faz f1 assumir o valor de f2
        f2 = fn  #faz f2 assumir o valor de fn

    return fn


# Programa Principal
n = int(input("Digite o valor de n: "))
resultado = fibonacci(n)
print(f"{resultado}")