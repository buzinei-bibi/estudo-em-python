#voto eleitoral 
idade = int(input("digite sua idade: "))
if idade < 16: 
    print("voto negado") 
elif idade >= 16 and idade < 18 or idade >= 70: 
   print("voto opcional") 

else:
    print("voto obrigatório")
    