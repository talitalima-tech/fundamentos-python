dados_alunos = {}

for i in range(10):
    nome = input()
    matricula = int(input())
    media = float(input())

    dados_alunos[nome] = {
        'matricula': matricula,
        'media': media
    }

aprovados = {}
reprovados = {}

for nome, aluno in dados_alunos.items():
    if aluno['media'] >= 5.0:
        print({
            'nome': nome,
            'matricula': aluno['matricula'],
            'media': aluno['media']
        })

for nome, aluno in dados_alunos.items():
    if aluno['media'] < 5.0:
        print({
            'nome': nome,
            'matricula': aluno['matricula'],
            'media': aluno['media']
        })