numero = []

while len(numero) < 12:
    num = int(input())
    if num not in numero:
        numero.append(num)
    else:
        print(f"Numero {num} ja existe, escreva outro")

print(numero)