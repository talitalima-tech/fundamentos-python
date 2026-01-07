def diferenca(x1, x2):
    C = []
    for i in range(len(x1)):
        C.append(x1[i] - x2[i])

    return C

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = diferenca(x1, x2)
print(y)