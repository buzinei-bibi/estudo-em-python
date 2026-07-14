# a tabela para guardar os registros 
tabela = []
def ler_txt():
    print ("\nlendo arquivo txt...")

    arquivo = open("aula.txt", "r" , encoding="utf-8")
    tabela.clear()  # limpa a tabela antes de ler novos dados 

    for linha in arquivo:
        linha = linha.strip()  # remove espaços em branco e quebras de linha 
        partes = linha.split(",")  # divide a linha em partes usando vírgula como separador

        registro = {
            "nome": partes[0],
            "idade": partes[1],
            "nota": partes[2]
        }

        tabela.append(registro)  # adiciona o registro à tabela
    arquivo.close()
    print("arquivo lido com sucesso!\n") 

def adicionar() :
    print("\nadicionar novo aluno:")
    nome = input("nome: ")
    idade = int(input("idade: "))
    nota = input("nota: ")

    registro = {
        "nome": nome,   
        "idade": idade,
        "nota": nota
    }
    tabela.append(registro)
    print("\naluno adicionado com sucesso!\n")

def listar() :
        print("\nlista de alunos:")

for aluno in tabela:
        print(f"nome:{aluno['nome']}, idade:{aluno['idade']}, nota:{aluno['nota']}") 


def gerar_csv():
    print("\ngerando arquivo relatório.csv...") 

    arquivo = open("relatorio.csv", "w", encoding="utf-8")
    arquivo.write("nome,idade,nota\n")  # cabeçalho do csv

    for aluno in tabela:
        linha = f"{aluno['nome']},{aluno['idade']},{aluno['nota']}\n"
        arquivo.write(linha)


    arquivo.close()
    print("arquivo relatório.csv gerado com sucesso!\n") 


def menu():
    while True:
        print("=== menu ===")
        print("1. ler arquivo txt")
        print("2. adicionar novo aluno")
        print("3. listar alunos")
        print("4. gerar_csv")
        print("5. sair")

        escolha = input("escolha uma opção: ") 

        if escolha == "1":
            ler_txt()
        elif escolha == "2":
            adicionar()
        elif escolha == "3":
            listar() 
        elif escolha == "4":
            gerar_csv()
        elif escolha == "5":
            print("saindo...")
            break 

        else:
         print("opção inválida! tente novamente.\n")