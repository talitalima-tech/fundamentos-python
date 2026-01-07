def numero_par(x):
    if x < 0:
        return

    numero_par(x - 2)

    print(x)


x = int(input(""))
numero_par(x)