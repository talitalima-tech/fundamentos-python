def inversão(num):
    unidade = num // 1 % 10
    dezena = num // 10 % 10
    centena = num // 100 % 10
    novo = unidade * 100 + dezena * 10 + centena * 1
    return novo


# Programa pricipal
numero = int(input('Número: '))
novo = inversão(numero)
print(novo)
