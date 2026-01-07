compromissos = []

for i in range(5):
    compromisso = input("Descricao: ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))

    compromisso_dict = {
        'compromisso': compromisso,
        'data': {
            'dia': dia,
            'mes': mes,
            'ano': ano
        }
    }
    compromissos.append(compromisso_dict)

while True:
    m = int(input())
    if m == 0:
        break
    a = int(input())

    compromissos_encontrados = []
    for c in compromissos:
        if c['data']['mes'] == m and c['data']['ano'] == a:
            compromissos_encontrados.append(c)

    compromissos_encontrados.sort(key=lambda x: x['data']['dia'])

    if compromissos_encontrados:
        for c in compromissos_encontrados:
            compromisso = c['compromisso']
            data_dict = c['data']
            print({
                'compromisso': compromisso,
                'data': data_dict
            })
    else:
        continue
