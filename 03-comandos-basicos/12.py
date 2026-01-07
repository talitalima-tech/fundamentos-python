def fatorial(x):
    fatorial = 1
    for i in range(1, x + 1):
        fatorial *= i
    return fatorial


def coeficiente_binominal(n, k):
    nf = fatorial(n)
    kf = fatorial(k)
    nkf = fatorial(n - k)
    binominal = nf / (kf * nkf)
    return binominal


# Programa Principal
n = int(input(""))
k = int(input(""))
binominal = coeficiente_binominal(n, k)
print(f"{binominal}")