nome_arquivo = input()

numero_telefone = []

with open(nome_arquivo, "r") as arquivo:
    for l in arquivo:
        nome, numero = l.strip().split('\t')
        numero_telefone.append({'nome': nome, 'telefone': numero})

contatos = sorted(numero_telefone, key=lambda x: x['nome'])
for n in contatos:
    print(n)

