alunos = []

limite_nomes = 5
limite_perguntas = 4

for i in range(limite_nomes):
    nome = input("Aluno: ")
    alunos.append(nome)

    if i < limite_nomes - 1:
        resposta = input("Deseja inserir novo aluno? [S/N] ").strip().upper()
        if resposta != "S":
            break

nome_pesquisa = input("Aluno para pesquisa: ").strip().lower()

for i, nome in enumerate(alunos):
    if nome_pesquisa in nome.lower():
        print(f"{nome}")
        print(f"{i}")

