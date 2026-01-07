arquivo_txt = input()
vogal = "AEIOUaeiou"
cont_vogal = 0
cont_consoante = 0
arquivo = open(arquivo_txt, "r")
conteudo = arquivo.read()

for letra in conteudo:
    if letra.isalpha():
        if letra in vogal:
            cont_vogal += 1
        else:
            cont_consoante += 1

print(f"{cont_vogal}")
print(f"{cont_consoante}")

arquivo.close()