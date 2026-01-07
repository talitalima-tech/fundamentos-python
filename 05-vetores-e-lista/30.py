def segmentos_maximos_iguais(x):
    for n in range(len(x)-1, 1, -1):
        numero = []
        for i in range((len(x)+1)-n):
            numero.append(x[i:(n+i)])
        for i in range(len(numero)):
            for j in range(1,(len(numero)-(i+1))+1):
                if numero[i]==numero[i+j]:
                    return i, i+j, n
    return -1, -1, -1


x = []
for i in range(10):
    x.append(int(input("")))
y1, y2, y3 = segmentos_maximos_iguais(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")