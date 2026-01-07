notas = []
soma = 0

for i in range(15):
    nota = float(input())
    notas.append(nota)

for n in notas:
    soma += n

media = soma / len(notas)
print(f"{media:.2f}")
