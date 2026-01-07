quant = 0
numero = int(input(""))
maior = numero
menor = numero
while quant < 9:
    quant += 1
    numero = int(input(""))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"{menor:.2f}")
print(f"{maior:.2f}")