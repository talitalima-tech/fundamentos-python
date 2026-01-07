def nao_repetido(x):
    unicos = []
    vistos = []
    for item in x:
        if item not in vistos:
            if x.count(item) == 1:
                unicos.append(item)
            vistos.append(item)

    return unicos

x = []
for i in range(10):
    x.append(int(input("")))
y = nao_repetido(x)
print(y)