import math
def eh_quadrado_perfeito(x):
    raiz = math.sqrt(x)
    if (raiz * raiz) == x:
        valor = True
    else:
        valor = False

    return valor

x = float(input(""))
y = eh_quadrado_perfeito(x)
print(f"{y}")
