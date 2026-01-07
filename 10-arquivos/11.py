def cont_texto(nome_arquivo, palavra):
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()

    contagem = conteudo.lower().count(palavra.lower())

    return contagem

nome_arquivo = input("")
palavra = input("")
resultado = cont_texto(nome_arquivo, palavra)
print(f"{resultado}")