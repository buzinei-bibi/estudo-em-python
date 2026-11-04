#registro de uma pessoa 
# 7 campos (atributos:informações)
# faça 4 adições via código
# faça 3 adições via input do usuário
# faça 2 atualizações via input do usuário
# faça 1 atualização via código 
# exiba o registro completo no final 

#7 campos (atributos:informações)

pessoa= { 
"nome" : "bianca" ,
" time" : "flamengo" , 
"idade" : 18 ,
"esporte fav" : "futebol" ,
"altura" : 1.65 ,
"desenho fav" : "pocoyo" ,
"cor fav" : "vermelho" , 
} 

#3 adições via input
chave1 = input("digite a chave que deseja adicionar ao registro da pessoa:")
valor1 = input("digite o valor correspondente a chave:")
pessoa[chave1] = valor1
chave2 = input("digite a chave que deseja adicionar ao registro da pessoa:")
valor2 = input("digite o valor correspondente a chave:")
pessoa[chave2] = valor2
chave3 = input("digite a chave que deseja adicionar ao registro da pessoa:")
valor3 = input("digite o valor correspondente a chave:")
pessoa[chave3] = valor3 

#2 atualização via input pelo usuário 
chave4 = input("digite a chave que deseja atualizar no registro da pessoa:")
valor4 = input("digite o novo valor correspondente a chave:")
pessoa[chave4] = valor4
chave5 = input("digite a chave que deseja atualizar no registro da pessoa:")
valor5 = input("digite o novo valor correspondente a chave:")
pessoa[chave5] = valor5

#faça 1 atualização via código
pessoa["esporte fav"] = "vôlei"

#exiba o registro completo no final
print("registro completo da pessoa:", pessoa)
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")