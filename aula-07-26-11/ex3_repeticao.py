#carrinho de compras simples
#crie uma lista chamada carrinho.
#depois:
#1.	adicione 4 produtos com append() (nomes de produtos, strings).
#2.	use insert() para colocar um produto no início da lista.
#3.	use pop() para remover o último item do carrinho.
#4.	exiba a quantidade de itens (len) e a lista final.

carinho = ["arroz", "feijão", "macarrão", "óleo"]
carinho.insert(0, "açúcar")
carinho.pop(3)
print("quantidade de itens:", len(carinho))
print("lista final:", carinho)

