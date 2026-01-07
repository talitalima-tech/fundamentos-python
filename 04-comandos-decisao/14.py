numero = 0
while True:
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")
    numero = int(input("numero"))

    if numero == 5:
        break

    num1 = float(input(""))
    num2 = float(input(""))

    if numero == 1:
        resposta = num1 + num2
    elif numero == 2:
        resposta = num1 - num2
    elif numero == 3:
        resposta = num1 * num2
    elif numero == 4:
        if num2 != 0:
            resposta = num1 / num2
        else:
            print("Erro")

print(f"{resposta:.2f}")

