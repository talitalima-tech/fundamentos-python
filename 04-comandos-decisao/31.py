def soma_eh_multiplicacao(x1, x2):
    soma = 0
    mult = 1

    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(x1, x2 + 1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i


    return soma, mult


x1 = int(input(""))
x2 = int(input(""))
soma, mult = soma_eh_multiplicacao(x1, x2)
print(f"{soma}")
print(f"{mult}")