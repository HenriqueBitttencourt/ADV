altura = float(input("Insira sua altura: "))
peso   = float(input("Insira seu peso: "))
pesoideal = (72.7 * altura) - 58
if peso > pesoideal:
    pesocerto = peso - pesoideal
    print("Você está acima do peso, para entrar no peso ideal, precisa perder: ")
    print("{0:.2f}".format(round(pesocerto, 2)))
if peso < pesoideal:
    pesocerto = pesoideal - peso
    print("Você está abaixo do peso, para atingir o ideal, precisa ganhar: ")
    print("{0:.2f}".format(round(pesocerto, 2)))
