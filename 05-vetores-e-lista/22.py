numero = []
tamanho = 100
n = 1

while len(numero) < tamanho:
    if n % 7 != 0 and n % 10 != 7:
        numero.append(n)
    n += 1

print(numero)