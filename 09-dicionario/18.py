estoque_mercado = []

for i in range(5):
    dados = {}
    dados['codigo'] = int(input())
    dados['nome'] = input()
    dados['preco'] = float(input())
    dados['quantidade'] = int(input())
    estoque_mercado.append(dados)

while True:

    for produto in estoque_mercado:
        print(produto)

    c = int(input())
    if c == 0:
        break
    q = int(input())

    encontrado = None
    for produto in estoque_mercado:
        if produto['codigo'] == c:
            encontrado = produto
            break

    if encontrado:
        if encontrado['quantidade'] >= q:
            encontrado['quantidade'] -= q
        else:
            print("Impossivel atender ao pedido, produto sem estoque suficiente")
    else:
        print("Impossivel atender ao pedido, codigo nao encontrado")
