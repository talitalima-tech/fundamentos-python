def media_ponderada(nota1, nota2):
    return (nota1 * 1.0 + nota2 * 2.0) / (1.0 + 2.0)

dados_alunos = []
n = int(input())
for i in range(n):
    aluno = {}

    aluno['matricula'] = int(input( ))
    aluno['nome'] = input()
    aluno['codigo'] = input()
    aluno['nota1'] = float(input())
    aluno['nota2'] = float(input())

    media = media_ponderada(aluno['nota1'], aluno['nota2'])
    aluno['media'] = media
    dados_alunos.append(aluno)

for aluno in dados_alunos:
    print(aluno)
