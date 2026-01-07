def uniao(x1, x2):
    numero = []
    for i in x1:
        if i not in numero:
            numero.append(i)
    for j in x2:
        if j not in numero:
            numero.append(j)

    return numero


x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = uniao(x1, x2)
print(y)