from datetime import datetime
nome = input()
endereco = input()
nascimento = input()
cidade = input()
cep = input()
email = input()
data_valida = len(nascimento) == 10 and nascimento[2] == "/" and nascimento[5] == "/"
if data_valida:
    dia_str = nascimento[:2]
    mes_str = nascimento[3:5]
    ano_str = nascimento[6:]
    if dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit():
        dia = int(dia_str)
        mes = int(mes_str)
        ano = int(ano_str)
        data_valida = (1 <= dia <= 31) and (1 <= mes <= 12) and (ano > 0)
    else:
        data_valida = False
cep_valido = (len(cep) == 10 and cep[2] == '.' and cep[6] == '-' and
               cep[:2].isdigit() and cep[3:6].isdigit() and cep[7:].isdigit())
email_valido = ("@" in email and "." in email and email.index('@') < email.index('.') and email.index('@') + 1 < email.rfind('.') and email.rfind('.') + 1 < len(email) and email.index('@') > 0  )
if not data_valida:
    print("Data errada")
elif not cep_valido:
    print("CEP errado")
elif not email_valido:
    print("E-mail errado")
else:
    dados = {'nome': nome,'endereco': endereco,'nascimento': nascimento,'cidade': cidade,'cep': cep,'email': email}
    print(dados)