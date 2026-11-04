#faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato:

preço1 = float(input("digite o preço do primeiro produto: R$ "))
preço2 = float(input("digite o preço do segundo produto: R$ "))
preço3 = float(input("digite o preço do terceiro produto: R$ "))
if preço1 <= preço2 and preço1 <= preço3:
    print("você deve comprar o primeiro produto, que custa R$ {:.2f}".format(preço1))
elif preço2 <= preço1 and preço2 <= preço3:
    print("você deve comprar o segundo produto, que custa R$ {:.2f}".format(preço2))
else:
    print("você deve comprar o terceiro produto, que custa R$ {:.2f}".format(preço3))
