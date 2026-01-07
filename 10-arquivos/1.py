nome_arquivo = "arq.txt"
arquivo = open(nome_arquivo, "w")
while True:
    linha = input()
    if linha == "0":
        break
    arquivo.write(linha + "\n")

arquivo.close()

arquivo = open(nome_arquivo, "r")
conteudo = arquivo.read()
print(conteudo)