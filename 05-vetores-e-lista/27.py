def eliminar_zero(x):
    compacto = []
    for i in x:
        if i != 0:
            compacto.append(i)

    return compacto


x = []
for i in range(10):
    x.append(int(input("")))
y = eliminar_zero(x)
print(y)