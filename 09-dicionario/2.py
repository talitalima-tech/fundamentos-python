consumo_carros = {}

for i in range(5):
    modelo = input()
    consumo = float(input())
    consumo_carros[modelo] = consumo

carro_economico = max(consumo_carros, key=consumo_carros.get)
print(f"Carro mais economico: {carro_economico}")

for c, consumo in consumo_carros.items():
    d = consumo * 50
    print(f"Carro {c} percorre {d:.2f} kms com 50 litros")

for c, consumo in consumo_carros.items():
    litros = 1000 / consumo
    print(f"Carro {c} precisa de {litros:.2f} litros para percorrer 1000 kms")
