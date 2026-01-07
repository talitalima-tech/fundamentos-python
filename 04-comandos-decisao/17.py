quadrado = None
cubo = None
raiz_quadrada = None

while True:
    n = int(input(""))
    if n <= 0:
        break

    quadrado = n ** 2
    cubo = n ** 3
    raiz_quadrada = n ** 0.5

print(f"{quadrado:.2f}")
print(f"{cubo:.2f}")
print(f"{raiz_quadrada:.2f}")
