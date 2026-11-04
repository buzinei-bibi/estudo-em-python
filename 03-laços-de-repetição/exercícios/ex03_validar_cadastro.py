#faça um programa que leia e valide as seguintes informações:

#nome: maior que 3 caracteres;
#idade: entre 0 e 150;
#salário: maior que zero;
#estado civil: 's', 'c', 'v', 'd';

while True:
    nome = input ("digite o seu nome: ")
    if len (nome) > 3:
        break
    else:
        print ("erro: o nome deve ter mais de 3 caracteres. tente novamente.")

while True:
    idade = int (input ("digite a sua idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print ("erro: a idade deve estar entre 0 e 150. tente novamente.")

while True:
    salario = float (input ("digite o seu salário: "))  
    if salario > 0:     
        break
    else:
        print ("erro: o salário deve ser maior que zero. tente novamente.")
while True:
    estado_civil = input ("digite o seu estado civil (s, c, v, d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print ("erro: estado civil inválido. tente novamente.") 

        print ("informações válidas cadastradas com sucesso!")
