nome = input()
idade = int(input())
sexo = input()
CPF = input()
data = input()
setor = int(input())
cargo = input()
salario = float(input())

dados_pessoais = {
    'nome': nome,
    'idade': idade,
    'sexo': sexo,
    'cpf': CPF,
    'nascimento': data,
    'setor': setor,
    'cargo': cargo,
    'salario': salario
}
print(dados_pessoais)
