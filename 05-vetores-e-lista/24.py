def intersecção(x1, x2):
    numero = []
    for i in x1:
        if i in x2:
            if i not in numero:
                numero.append(i)

    return numero


x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = intersecção(x1, x2)
print(y)