def soma_numero(x):
    if x == 1:
        return 1
    else:
        return x + soma_numero(x - 1)


x = int(input(""))
y = soma_numero(x)
print(f"{y}")