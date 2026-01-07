dados_pessoas = []


def inserir_pessoa():
    nome = input("Nome: ")
    email = input("E-mail: ")
    rua = input("Rua: ")
    numero = int(input("Numero: "))
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("Pais: ")
    ddd = int(input("DDD: "))
    telefone = input("Telefone: ")
    dia_niver = int(input("Dia do nascimento: "))
    mes_niver = int(input("Mes do nascimento: "))
    ano_niver = int(input("Ano do nascimento: "))
    observacao = input("Observacao: ")

    dados_pessoa = {
        'nome': nome,
        'email': email,
        'endereco': {
            'rua': rua,
            'numero': numero,
            'complemento': complemento,
            'bairro': bairro,
            'cep': cep,
            'cidade': cidade,
            'estado': estado,
            'pais': pais
        },
        'telefone': {
            'ddd': ddd,
            'numero': telefone
        },
        'nascimento': {
            'dia': dia_niver,
            'mes': mes_niver,
            'ano': ano_niver
        },
        'observacao': observacao
    }

    dados_pessoas.append(dados_pessoa)


def encontrar_primeiro_nome():
    nome1 = input("Primeiro nome: ")
    if not nome1:
        return []

    return [dados for dados in dados_pessoas if dados['nome'].split()[0].lower().startswith(nome1.lower())]


def encontrar_mes_nascimento():
    mes_busca = int(input("Mes de nascimento: "))
    return [dados for dados in dados_pessoas if dados['nascimento']['mes'] == mes_busca]


def encontrar_dia_mes_nascimento():
    dia_buscar = int(input("Dia do nascimento: "))
    mes_buscar = int(input("Mes do nascimento: "))
    return [
        dados for dados in dados_pessoas
        if dados['nascimento']['dia'] == dia_buscar and dados['nascimento']['mes'] == mes_buscar
    ]


def imprimir_agenda(opcao):
    if opcao == 1:
        return [
            {
                'nome': dados['nome'],
                'telefone': dados['telefone'],
                'email': dados['email']
            } for dados in dados_pessoas
        ]
    elif opcao == 2:
        return dados_pessoas

    return []


def menu():
    while True:
        print("1: Inserir uma pessoa")
        print("2: Buscar por primeiro nome")
        print("3: Buscar por mes de nascimento")
        print("4: Buscar por dia e mes de nascimento")
        print("5: Imprimir agenda")
        print("0: Sair")

        n = int(input("Opcao: "))

        if n == 0:
            break
        elif n == 1:
            inserir_pessoa()
        elif n == 2:
            resultados = encontrar_primeiro_nome()
            for dado in resultados:
                print(dado)
        elif n == 3:
            resultados = encontrar_mes_nascimento()
            for dado in resultados:
                print(dado)
        elif n == 4:
            resultados = encontrar_dia_mes_nascimento()
            for dado in resultados:
                print(dado)
        elif n == 5:
            print("1: Imprimir apenas nome, telefone e email")
            print("2: Imprimir todos os dados")
            opcao_impressao = int(input("Opcao: "))
            if opcao_impressao < 1 or opcao_impressao > 2:
                print("Opcao invalida")
            resultados = imprimir_agenda(opcao_impressao)
            for dado in resultados:
                print(dado)
        elif n < 0 or n >= 6:
            print("Opcao invalida")


# Executar o menu principal
menu()
