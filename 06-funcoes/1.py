# recebe número inteiro e mostrar o dobro
def dobro(num):
    d = num * 2
    return d

# Programa principal
numero = int(input("numero: "))
numero = dobro(numero)
print(f'{numero}')