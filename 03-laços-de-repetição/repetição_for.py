#estrutura de repetição for 

#repeat ou repita 3 vezes 

for numero in range(3): 

    print("direita")

#para + variável + em + intervalo (número de repetições)

for numero in range(1,4):

    print("direita")

    for numero in range(0,10,2): # 0 até 9 de 2 em 2
 
        print(numero)


#lista de elementos

frutas = ["maçã", "banana", "laranja"]
números = [1, 2, 3, 4, 5]

for fruta in frutas:

    print(fruta) 

for número in números:

    print(número) 

#contagem de caracteres em uma string com len ( )

nome = "python" #6 letras = elementos   # 0 1 2 3 4 5 
tamanho = len (nome) #len = length = comprimento
for i in range(tamanho): # index = posição 

    print(f"índice {i} tem a letra {nome[i]}")  