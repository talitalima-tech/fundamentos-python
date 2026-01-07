import string

nome_arquivo = input("")

cont_cada_letra = {letra: 0 for letra in string.ascii_lowercase}
cont_letras = 0
cont_linhas = 0
cont_palavras = 0

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        cont_linhas += 1

        palavras = linha.split()
        cont_palavras += len(palavras)

        cont_letras += len(linha)

        for c in linha:
            if c.isalpha():
                letra = c.lower()
                if letra in cont_cada_letra:
                    cont_cada_letra[letra] += 1

print(f"{cont_letras}")
print(f"{cont_linhas}")
print(f"{cont_palavras}")

for l, quant in cont_cada_letra.items():
    print(f"{l}: {quant}")


