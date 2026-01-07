def funcao():
    maior = None
    menor = None
    while True:
        numero = int(input(""))

        if numero < 0:
            break

        if maior is None:
            maior = numero
        elif numero > maior:
            maior = numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero

    return maior, menor


x, y = funcao()

if x is None:
    if y is None:
        print("")
else:
    print(x)
    print(y)