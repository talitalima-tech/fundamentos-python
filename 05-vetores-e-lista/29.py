def ordenar_decrescente(x):
    numero = x[:]
    n = len(numero)

    for i in range(n):
        maior = i
        for j in range(i + 1, n):
            if numero[j] > numero[maior]:
                maior = j

        numero[i], numero[maior] = numero[maior], numero[i]

    return numero


x = []
for i in range(10):
    x.append(int(input("")))
y = ordenar_decrescente(x)
print(y)