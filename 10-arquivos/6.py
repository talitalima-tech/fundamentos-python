import string

nome_arquivo = input("")

contagem = {letra: 0 for letra in string.ascii_lowercase}

with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

for c in conteudo:
    if c.isalpha():
        letra = c.lower()
        contagem[letra] += 1


for l, quant in contagem.items():
    print(f"{l}: {quant}")

