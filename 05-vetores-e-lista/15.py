numero = []
for i in range(10):
    num = int(input())
    numero.append(num)

numero_repetido = []
for i in range(len(numero)):
    for j in range(i + 1, len(numero)):
        if numero[i] == numero[j]:
            numero_repetido.append(numero[i])

if numero_repetido:
    for n in numero_repetido:
        print(n)
