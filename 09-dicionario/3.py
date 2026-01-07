dados_alunos = {}
n = int(input())
for i in range(n):
    dados_alunos['nome'] = input()
    dados_alunos['matricula'] = int(input())
    dados_alunos['curso'] = input()
    print(dados_alunos)
