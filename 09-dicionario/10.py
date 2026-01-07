dados_pessoas = {}

for i in range(5):
    nome = input()
    endereco = input()
    telefone = input()
    dados_pessoas[nome] = {
        'endereco': endereco,
        'telefone': telefone
    }

nomes = sorted(dados_pessoas.keys())
for n in nomes:
      print({
            'nome': n,
            'endereco': dados_pessoas[n]['endereco'],
            'telefone': dados_pessoas[n]['telefone']
        })
