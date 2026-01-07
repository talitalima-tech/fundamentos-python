def soma_quadrado(n1, n2, n3):
    soma = (n1 ** 2) + (n2 ** 2) + (n3 ** 2)
    quadrado = (n1 + n2 + n3) ** 2
    return soma, quadrado


# Programa principal
num1 = float(input('número: '))
num2 = float(input('número: '))
num3 = float(input('número: '))
soma, quadrado = soma_quadrado(num1, num2, num3)
print(f'{soma:.2f}')
print(f'{quadrado:.2f}')
