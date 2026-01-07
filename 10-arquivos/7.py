nome = input()

with open(nome, "r") as arquivo:
    conteudo = arquivo.read()

novo_conteudo = ""
vogal = "AEIOUaeiou"

for c in conteudo:
    if c in vogal:
        novo_conteudo += "*"
    else:
        novo_conteudo += c

novo_nome = nome + ".out"
with open(novo_nome, "w") as arquivo_saida:
    arquivo_saida.write(novo_conteudo)

with open(novo_nome, "r") as arquivo_saida:
    print(arquivo_saida.read())