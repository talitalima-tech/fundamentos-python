palavra = input("")
caractere = input("")
vogais = "aeiouAEIOU"
cont = 0
saida= ""
for c in palavra:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
       c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        cont += 1
        saida += caractere
    else:
        saida += c
print(cont)
print(saida)