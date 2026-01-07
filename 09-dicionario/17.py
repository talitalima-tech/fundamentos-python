consumo_energia = []

for i in range(5):
    dados = {}
    dados['nome'] = input()
    dados['potencia'] = float(input())
    dados['tempo'] = float(input())

    consumo_energia.append(dados)

t = int(input())

consumo_total = 0
consumo_individual = []

for dados in consumo_energia:
    consumo = dados['potencia'] * dados['tempo'] * t
    consumo_individual.append(consumo)
    consumo_total += consumo

print(f"{consumo_total:.2f}")

for i, dados in enumerate(consumo_energia):
    consumo_relativo = (consumo_individual[i] / consumo_total) * 100
    print(f"{dados['nome']}: {consumo_relativo:.2f}")

