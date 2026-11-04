# variável e tipos de dados 
nome = "bianca" #o sinal de igual (=) é o operador de atribuição
idade = 19 #int (inteiro)
cidade_uf = "sjc-sp" \
 
# o que não fazer na declaração de variáveis 
# 1 não usar espaço em branco nome da variável
# 2 não começar o nome da variável com número 
# 3 não usar caracteres especiais (ex:!,@,#)
# 4 não usar palavra reservadas da linguagem (ex:print, input)
# 5 não usar acentuação no nome da variável

#print ("nome:", nome)
#print ("idade:", idade)
#print ("cidade")
#print ("nome:",nome)

"meu nome é bianca"
"minha idade é 19 anos"
"eu moro em sjc"

print ("meu nome é bianca")
print ("minha idade é 19 anos")
print ("eu moro em sjc")


print ("meu nome é", nome, "minha idade é", idade, "eu moro", cidade_uf) 

#frase para print e variável sempre condizente com o valor

#concatenação de strings 

print ("meu nome é " + nome +
 "minha idade é " + str(idade) + "." )  

print (f"meu nome é {nome}. minha idade é {idade}.")
#f-string (formatação de string)
