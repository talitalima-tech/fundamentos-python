def produto(num):
    p = 1
    for n in num:
        p *= n
    return p


def encontrar_direcao(matriz, linha, coluna, direcao):
    num = []
    for i in range(4):
        linha_nova = linha + i * direcao[0]
        coluna_nova = coluna + i * direcao[1]
        if 0 <= linha_nova < 20 and 0 <= coluna_nova < 20:
            num.append(matriz[linha_nova][coluna_nova])
        else:
            return 0, None, None, None
    return produto(num), linha, coluna, direcao


def maior_produto(matriz):
    direcoes = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]

    produto_maior = 0
    posicao = (0, 0)
    melhor_direcao = ""

    for linha in range(20):
        for coluna in range(20):
            for d in direcoes:
                produto, linha1, coluna1, d = encontrar_direcao(matriz, linha, coluna, direcao)
                if produto > produto_maior:
                    produto_maior = produto
                    posicao = (linha, coluna)
                    if d == (0, 1):
                        melhor_direcao = "direita"
                    elif d == (1, 0):
                        melhor_direcao = "baixo"
                    elif d == (1, 1):
                        melhor_direcao = "direita baixo"
                    elif d == (1, -1):
                        melhor_direcao = "esquerda baixo"

    return produto_maior, posicao, melhor_direcao


matriz = []
for l in range(20):
    linha = []
    for c in range(20):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

produto_max, posicao1, direcao = maior_produto(matriz)
print(produto_max)
print(posicao1[0])
print(posicao1[1])
print(direcao)
