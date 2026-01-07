carros = []

for i in range(5):
    dados = {}

    dados['modelo'] = input()
    dados['ano'] = int(input())
    dados['preco'] = float(input())

    carros.append(dados)

encontrados = []
while True:
    p = int(input())
    if p == 0:
        break

    for dados in carros:
        if p > dados['preco']:
            encontrados.append(dados)

if encontrados:
    for c in encontrados:
        print(c)
else:
    print("")