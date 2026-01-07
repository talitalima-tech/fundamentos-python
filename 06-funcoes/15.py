def separação(numero):
    unidade = numero // 1 % 10
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000 % 10
    a = milhar
    b = centena
    c = dezena
    d = unidade
    return a, b, c, d

# Programa principal
numero = int(input('Número: '))
a, b, c, d = separação(numero)
print(a, b, c, d)