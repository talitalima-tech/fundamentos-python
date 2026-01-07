def maior_menor():
    maior = None
    menor = None
    quant = 0
    n = int(input(""))
    while quant < n:
        numero = float(input(""))
        quant += 1

        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero

    return menor, maior


x, y = maior_menor()

if x is None:
    if y is None:
        print("")
else:
    print(f"{x:.2f}")
    print(f"{y:.2f}")