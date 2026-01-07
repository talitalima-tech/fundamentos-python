quant = 0
maior = None
vezes = 0
numero = int(input(""))
while quant < numero:
    n = int(input(""))

    if maior is None:
        maior = n
        vezes = 1
    else:
        if n > maior:
            maior = n
            vezes = 1
        elif n == maior:
            vezes += 1
    quant += 1

print(maior)
print(vezes)