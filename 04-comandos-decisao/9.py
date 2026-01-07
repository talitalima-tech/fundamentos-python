num1 = float(input(""))
num2 = float(input(""))
num3 = float(input(""))
maior=None
menor=None
meio=None

if num1 <= num2 <= num3:
    menor, meio, maior = num1, num2, num3
elif num1 <= num3 <= num2:
    menor, meio, maior = num1, num3, num2
elif num2 <= num1 <= num3:
    menor, meio, maior = num2, num1, num3
elif num2 <= num3 <= num1:
    menor, meio, maior = num2, num3, num1
elif num3 <= num1 <= num2:
    menor, meio, maior = num3, num1, num2
else:
    menor, meio, maior = num3, num2, num1


print(f"{menor:.2f}")
print(f"{meio:.2f}")
print(f"{maior:.2f}")