soma = 0
quant = 0
while True:
    numero = int(input(""))
    if numero > 0:
        quant += 1
        soma += numero
        if quant == 10:
            media = soma / quant
            break

print(f"{media:.2f}")