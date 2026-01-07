def MMC(x1, x2):
    # inicia com o numero maior
    resultado = max(x1, x2)

    while not (resultado % x1 == 0 and resultado % x2 == 0):
        resultado += 1  # Aumenta o resultado até encontrar o MMC

    return resultado

x1 = int(input(""))
x2 = int(input(""))
y = MMC(x1, x2)
print(f"{y}")