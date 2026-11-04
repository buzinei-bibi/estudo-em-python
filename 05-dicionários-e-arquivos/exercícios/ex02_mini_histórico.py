#exercício 2

#crie um mini histórico: pergunte qual é nome do usuário e qual é a mensagem
#armazenar as informações digitadas pelo usuário no dicionário histórico

historico = []
nome = input("qual é seu nome: ")
mensagem = input("digite sua mensagem: ")

dicionario = {
    "user" : nome,
    "quero dizer" : mensagem

}

historico.append(dicionario)
print(historico)
