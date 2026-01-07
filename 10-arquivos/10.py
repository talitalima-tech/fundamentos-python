nome_arquivo = input()
nome_saida = input()

cidades = []

with open(nome_arquivo, "r") as arquivo:
    for l in arquivo:
        cidade, habitantes = l.strip().split('\t')
        cidades.append({'nome': cidade, 'habitantes': int(habitantes)})

for c in cidades:
    print(c)

mais_populosa = max(cidades, key=lambda x: x['habitantes'])

with open(nome_saida, "w") as arquivo_saida:
    arquivo_saida.write(f"{mais_populosa['nome']}\t{mais_populosa['habitantes']}\n")

print(f"{mais_populosa['nome']}\t{mais_populosa['habitantes']}")


