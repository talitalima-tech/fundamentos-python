nome_entrada = input("")
nome_saida = input("")

with open(nome_entrada, "r") as arquivo_entrada:
    conteudo = arquivo_entrada.read()

novo_conteudo = conteudo.upper()

with open(nome_saida, "w") as arquivo_saida:
    arquivo_saida.write(novo_conteudo)

print(conteudo, end="")
print(novo_conteudo)

