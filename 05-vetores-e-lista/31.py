nome = input()
nome = nome.replace(" ", "")

encontrada = []

for letra in nome:
    # Verifica se a letra é alfabética e não foi encontrada
    if letra.isalpha() and letra not in encontrada:
        encontrada.append(letra)


print(len(encontrada))
