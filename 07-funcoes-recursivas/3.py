def soma_n_cubo(x):
    if x == 1:
        return 1
    else:
        return (x ** 3) + soma_n_cubo(x - 1)


x = int(input(""))
y = soma_n_cubo(x)
print(f"{y}")