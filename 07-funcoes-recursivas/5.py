def funcao(x):
    if x < 0:
        return

    funcao(x - 1)

    print(x)


x = int(input(""))
funcao(x)