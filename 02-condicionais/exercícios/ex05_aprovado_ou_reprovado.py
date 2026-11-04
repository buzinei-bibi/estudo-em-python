#faça um programa para a leitura de duas notas parciais de um aluno. 
# o programa deve calcular a média alcançada por aluno e apresentar:
# a mensagem "aprovado", se a média alcançada for maior ou igual a 7;
# a mensagem "reprovado", se a média for menor do que 7;
# a mensagem "aprovado com distinção", se a média for igual a 10.

nota_1 = float(input("digite a nota 1: "))
nota_2 = float(input("digite a nota 2: "))
média= (nota_1 + nota_2) /2
if média == 10:
    print("aprovado com distinção")
elif média >= 7:
    print("aprovado")
else:
    print("reprovado")