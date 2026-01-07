import random

def imprime_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    for i in range(n):
        print(" " + " | ".join(tabuleiro[i]) + " ")
        if i < n - 1:
            print("---+---+---")

def inicializa_tabuleiro(n):
    return [[" " for _ in range(n)] for _ in range(n)]

def jogada_realizada(t, l, c, j):
    if t[l][c] == " ":
        t[l][c] = j
        return True
    return False

def resultado(tabuleiro):
    n = len(tabuleiro)
    for i in range(n):
        if all(tabuleiro[i][j] == "X" for j in range(n)) or all(tabuleiro[j][i] == "X" for j in range(n)):
            return "Que droga, você ganhou."
        if all(tabuleiro[i][j] == "O" for j in range(n)) or all(tabuleiro[j][i] == "O" for j in range(n)):
            return "Eu ganhei!"

    if all(tabuleiro[i][i] == "X" for i in range(n)) or all(tabuleiro[i][n - 1 - i] == "X" for i in range(n)):
        return "Que droga, você ganhou."
    if all(tabuleiro[i][i] == "O" for i in range(n)) or all(tabuleiro[i][n - 1 - i] == "O" for i in range(n)):
        return "Eu ganhei!"

    if all(tabuleiro[i][j] != " " for i in range(n) for j in range(n)):
        return "Empate!"

    return None

def computador_jogar(tabuleiro):
    n = len(tabuleiro)
    while True:
        linha = random.randint(0, n - 1)
        coluna = random.randint(0, n - 1)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "O"
            print(f"Vou jogar na linha {linha + 1} e coluna {coluna + 1}.")
            break

def jogar(tabuleiro, jogador_comeca):
    imprime_tabuleiro(tabuleiro)

    if jogador_comeca == "Humano":
        print("Sua vez de jogar.")
        while True:
            l = int(input(f"Qual linha?")) - 1
            c = int(input(f"Qual coluna?")) - 1
            if l < 0 or l >= len(tabuleiro) or c < 0 or c >= len(tabuleiro):
                print("Posição inválida, por favor digite novamente.")
            elif not jogada_realizada(tabuleiro, l, c, "X"):
                print("Posição já ocupada, por favor, digite novamente.")
            else:
                break

        jogador_comeca = "Computador"
    else:
        print("Minha vez de jogar.")
        computador_jogar(tabuleiro)
        jogador_comeca = "Humano"

    res = resultado(tabuleiro)
    if res:
        imprime_tabuleiro(tabuleiro)
        print(res)
    else:
        jogar(tabuleiro, jogador_comeca)

print("Vamos começar.")
n = 3
tabuleiro = inicializa_tabuleiro(n)
jogador_comeca = random.choice(["Humano", "Computador"])
jogar(tabuleiro, jogador_comeca)
