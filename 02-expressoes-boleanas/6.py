idade= int(input(""))
tempo= int(input(""))
if (idade >= 65) or (tempo >= 30) or (idade >= 60 and tempo>=25):
    print("Pode se aposentar")
else:
    print("Nao pode se aposentar")