saque = int(input())
nota100 = saque // 100
resto100 = saque % 100
nota50 = resto100 // 50
resto50 = resto100 % 50
nota20 = resto50 // 20
resto20 = resto50 % 20
nota10 = resto20 // 10
resto10 = resto20 % 10
nota5 = resto10 // 5
resto5 = resto10 % 5
nota2 = resto5 // 2
resto2 = resto5 % 2
nota1 = resto2 // 1
print(f"{nota100}")
print(f"{nota50}")
print(f"{nota20}")
print(f"{nota10}")
print(f"{nota5}")
print(f"{nota2}")
print(f"{nota1}")