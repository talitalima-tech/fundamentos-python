# Antecessor e sucessor
def antecessor_sucessor(num):
    a = num - 1
    s = num + 1
    return a, s


# Programa principal
numero = int(input('número: '))
antecessor, sucessor = antecessor_sucessor(numero)
print(antecessor)
print(sucessor)