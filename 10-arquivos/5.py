nome_arquivo = input()
caractere = input()
arquivo = open(nome_arquivo, "r")
conteudo = arquivo.read()
cont_letra = 0

for letra in conteudo:
    if letra == caractere:
        cont_letra += 1

print(cont_letra)
arquivo.close()