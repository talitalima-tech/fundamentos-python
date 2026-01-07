def potencia(x1, x2):
    if x2 == 0:
        return 1
    if x2 == 1:
        return x1
    else:
        return x1 * potencia(x1, x2 -1)


x1 = int(input(""))
x2 = int(input(""))
y = potencia(x1, x2)
print(f"{y}")