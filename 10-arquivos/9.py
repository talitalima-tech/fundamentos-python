nome_entrada1 = input("")
nome_entrada2 = input("")

with open(nome_entrada1, "r") as arquivo_entrada1:
    conteudo1 = arquivo_entrada1.read()

with open(nome_entrada2, "r") as arquivo_entrada2:
    conteudo2 = arquivo_entrada2.read()

nome_saida = nome_entrada1 + "_" + nome_entrada2

with open(nome_saida, "w") as arquivo_saida:
    arquivo_saida.write(conteudo1)
    arquivo_saida.write(conteudo2)

with open(nome_saida, "r") as arquivo_saida:
    print(arquivo_saida.read())


