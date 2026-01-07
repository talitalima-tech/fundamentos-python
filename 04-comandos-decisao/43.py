nome = input("")
idade = int(input(""))
if idade < 0:
    print()
else:
    nome_velho = novo_nome = nome
    idade_velho = idade_nova = idade

    while True:
        nome = input("")
        idade = int(input(""))

        if idade < 0:
            break

        else:
            if idade < idade_nova:
                idade_nova = idade
                novo_nome = nome

            if idade > idade_velho:
                idade_velho = idade
                nome_velho = nome

print(novo_nome)
print(idade_nova)
print(nome_velho)
print(idade_velho)