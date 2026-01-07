dados_pessoais = []

for i in range(5):
    nome = input("Nome: ")
    rua = input("Rua: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    salario = float(input("Salario: "))
    identidade = input("Identidade: ")
    cpf = input("CPF: ")
    estado_civil = input("Estado Civil: ")
    telefone = input("Telefone: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")

    dados_pessoa = {
        'nome': nome,
        'endereco': {
            'rua': rua,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
        },
        'salario': salario,
        'identidade': identidade,
        'cpf': cpf,
        'civil': estado_civil,
        'telefone': telefone,
        'idade': idade,
        'sexo': sexo
    }

    dados_pessoais.append(dados_pessoa)

maior_idade = max(dados_pessoais, key=lambda pessoa: pessoa['idade'])
print("Pessoa com maior idade:")
print(maior_idade)

encontrado_masculino = [dados for dados in dados_pessoais if dados['sexo'].lower() == 'masculino']
print("Pessoas do sexo masculino:")
for pessoa in encontrado_masculino:
    print(pessoa)

encontrado_salario = [dados for dados in dados_pessoais if dados['salario'] > 1000]
print("Pessoas com salario maior que 1000:")
for pessoa in encontrado_salario:
    print(pessoa)

valor = input("Identidade: ")
i_encontrado = [dados for dados in dados_pessoais if dados['identidade'] == valor]

if i_encontrado:
    for pessoa in i_encontrado:
        print(pessoa)

