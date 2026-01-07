numero = []
tamanho = 70
n = 0
while len(numero) < tamanho:
     for i in range(tamanho):
        valor = (i + 5 * i) % (i + 1)
        numero.append(valor)
print(numero)