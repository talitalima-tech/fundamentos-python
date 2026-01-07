livros = []

for i in range(5):
    dados = {}

    dados['titulo'] = input()
    dados['autor'] = input()
    dados['ano'] = int(input())

    livros.append(dados)

nome = input()
encontrados = []
for dados in livros:
    if nome.lower() in dados['titulo'].lower():
        encontrados.append(dados)

if encontrados:
    for l in encontrados:
        print(l)
else:
    print("")