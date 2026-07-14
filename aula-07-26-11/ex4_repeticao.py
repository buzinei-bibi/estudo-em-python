#inserir, ordenar e remover itens da lista
#crie uma lista vazia chamada numeros.
#depois:
#1.	use append() para adicionar 5 números escolhidos pelo usuário.
#2.	ordene a lista com sort().
#3.	remova o maior valor usando pop() ou remove().
#4.	mostre o resultado final.

numeros=[]
for i in range(5):
    num=int(input("digite um número inteiro:"))
    numeros.append(num)
numeros.sort()
print("lista ordenada:", numeros)
numeros.pop()  #remove o maior valor que está no final da lista ordenada
print("lista final após remover o maior valor:", numeros)
#outra opção seria usar remove(max(numeros)) para remover o maior valor
#numeros.remove(max(numeros))
#print("lista final após remover o maior valor:", numeros)