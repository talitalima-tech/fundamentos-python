def soma_vetor(v1, v2):
    return {
        'x': v1['x'] + v2['x'],
        'y': v1['y'] + v2['y'],
        'z': v1['z'] + v2['z']
    }


vetor1 = {}
vetor2 = {}

vetor1['x'] = float(input())
vetor1['y'] = float(input())
vetor1['z'] = float(input())

vetor2['x'] = float(input())
vetor2['y'] = float(input())
vetor2['z'] = float(input())

resultado = soma_vetor(vetor1, vetor2)

print(resultado)