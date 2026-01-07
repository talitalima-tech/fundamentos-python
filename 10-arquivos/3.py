arquivo_txt = input()
vogal = "AEIOUaeiou"
cont_vogal = 0

arquivo = open(arquivo_txt, "r")
conteudo = arquivo.read()

for letra in conteudo:
    if letra.isalpha():
        if letra in vogal:
            cont_vogal += 1

print(f"{cont_vogal}")

arquivo.close()