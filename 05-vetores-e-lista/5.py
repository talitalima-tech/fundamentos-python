conjunto = []

for i in range(10):
    num = float(input())
    conjunto.append(num)

for q in conjunto:
    print(f"{q:.2f}")

for q in conjunto:
    quadrado = q ** 2
    print(f"{quadrado:.2f}")