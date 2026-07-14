#limpando lista de repetidos
#dada uma lista com valores repetidos, como:

#valores = [4, 2, 4, 7, 2, 9, 4]
#faça:

#1.	remova apenas a primeira ocorrência do valor 4 usando remove().
#2.	remova o valor da posição 2 usando pop(2).
#3.	use append() para adicionar um valor novo.
#4.	mostre a lista final.

valores = [4, 2, 4, 7, 2, 9, 4]
valores.remove(4)
valores.pop(2)
valores.append(10)
print("lista final:", valores)

