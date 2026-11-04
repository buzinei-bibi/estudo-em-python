#criação de registro de um carro
carro = {
    "marca": "toyota",
    "modelo": "corolla",
    "ano": 2020,
} 

#criação de um dicionário vazio 
dicionario_vazio = {} 

#adição de novos pares chave-valor ao dicionário
carro["cor"] = "prata"
carro["preço"] = 85000.00 


#adição/atualização pelo usuário no carro 
chave = input("digite a chave que deseja adicionar ao carro:") 
valor = input("digite o valor correspondente a chave:")
carro[chave] = valor 

#exibição do dicionário atualizado
print("dicionário atualizado do carro:", carro)
for chave, valor in carro.items():
    print(f"{chave}: {valor}") 