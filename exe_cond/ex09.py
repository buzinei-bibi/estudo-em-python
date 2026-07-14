#faça um programa que leia três números e mostre-os em ordem decrescente:

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("ordem decrescente:", num1, num2, num3)
    else:
        print("ordem decrescente:", num1, num3, num2)

elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("ordem decrescente:", num2, num1, num3)
    else:
        print("ordem decrescente:", num2, num3, num1)
else:
    if num1 >= num2:
        print("ordem decrescente:", num3, num1, num2)
    else:
        print("ordem decrescente:", num3, num2, num1)
