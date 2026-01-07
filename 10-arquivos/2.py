arquivo_txt = input()

arquivo = open(arquivo_txt, "r")
conteudo = arquivo.read()
cont_linhas = 0

cont_linhas = conteudo.count('\n')

arquivo.close()
print(cont_linhas)
