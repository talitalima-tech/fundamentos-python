from datetime import datetime

nome_arquivo = input("")
dia = int(input(""))
mes = int(input(""))
ano= int(input(""))

nome_arquivo_saida = f"{nome_arquivo}.out"

with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

resultados = []

for l in linhas:
    partes = l.strip().split('\t')
    nome = partes[0]
    dia_nascimento, mes_nascimento, ano_nascimento = map(int, partes[1].split())

    idade = ano - ano_nascimento
    if (mes < mes_nascimento) or (mes == mes_nascimento and dia < dia_nascimento):
        idade -= 1

    resultados.append(f"{nome}\t{idade}\n")

with open(nome_arquivo_saida, 'w') as arquivo_saida:
    arquivo_saida.writelines(resultados)

with open(nome_arquivo_saida, 'r') as arquivo_saida:
    conteudo = arquivo_saida.read()

print(conteudo)
