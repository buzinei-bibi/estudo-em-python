#faça um programa que peça uma nota, entre zero e dez. mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True: 
    nota = float(input("digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"nota válida: {nota}")
        break
    else:
        print("valor inválido. tente novamente.")