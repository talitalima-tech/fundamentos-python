import math
numero = float(input(""))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"{raiz:.2f}")
else:
    print("Numero Invalido")