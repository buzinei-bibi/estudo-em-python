#faça um programa que leia três números e mostre o maior e o menor deles

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
num3 = float(input("digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    print("o maior número é:", num1)
    if num2 <= num3:
        print("o menor número é:", num2)
    else:
        print("o menor número é:", num3)
elif num2 >= num1 and num2 >= num3:
    print("o maior número é:", num2)
    if num1 <= num3:
        print("o menor número é:", num1)
    else:
        print("o menor número é:", num3)
else:
    print("o maior número é:", num3)
    if num1 <= num2:
        print("o menor número é:", num1)
    else:
        print("o menor número é:", num2)
        