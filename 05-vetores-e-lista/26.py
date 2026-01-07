def diferenca(x1, x2):
    dif = []
    for i in x1:
        for j in x2:
            if i not in dif:
                if i not in x2:
                    dif.append(i)

    return dif


x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = diferenca(x1, x2)
print(y)