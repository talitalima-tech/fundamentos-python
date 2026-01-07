def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


dados_alunos = {}

for i in range(5):
    matricula = int(input())
    nome = input()
    prova1 = float(input())
    prova2 = float(input())
    prova3 = float(input())

    dados_alunos[matricula] = {
        'nome': nome,
        'notas': [prova1, prova2, prova3],
        'media': media(prova1, prova2, prova3)
    }

maior_nota1 = max(dados_alunos.values(), key=lambda aluno: aluno['notas'][0])
maior_media = max(dados_alunos.values(), key=lambda aluno: aluno['media'])
menor_media = min(dados_alunos.values(), key=lambda aluno: aluno['media'])

print(f"Aluno {maior_nota1['nome']} tem a maior nota1: {maior_nota1['notas'][0]:.2f}")
print(f"Aluno {maior_media['nome']} tem a maior media: {maior_media['media']:.2f}")
print(f"Aluno {menor_media['nome']} tem a menor media: {menor_media['media']:.2f}")

for aluno in dados_alunos.values():
    if aluno['media'] >= 7:
        print(f"Aluno {aluno['nome']} esta aprovado com media {aluno['media']:.2f}")
    else:
        print(f"Aluno {aluno['nome']} esta reprovado com media {aluno['media']:.2f}")

