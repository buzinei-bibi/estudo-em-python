#faça um programa que leia um nome de usuário e a
# sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input ("digite o nome de usuário: ")
    senha = input ("digite a senha:")
    if senha == usuario:
        print ("erro: a senha não pode ser igual ao nome de usuário. tente novamente.")
    else:
        print ("usuaário e senha cadastrados com sucesso!")
        break

    