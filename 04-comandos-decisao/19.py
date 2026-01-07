def numero_positivo_negativo(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0

x = int(input(""))
y = numero_positivo_negativo(x)
print(y)