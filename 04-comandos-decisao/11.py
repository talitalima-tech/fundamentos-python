num1 = float(input())
operacao = input()
num2 = float(input())

if operacao == "+":
    resposta = num1 + num2
elif operacao == "-":
    resposta = num1 - num2
elif operacao == "*":
    resposta = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("erro")
    else:
        resposta= num1/num2
else:
    print("erro")
print(f"{resposta:.2f}")