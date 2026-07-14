#faça um programa para uma loja de tintas
#o programa deverá pedir o tamanho em metros quadrados da área a ser pintada
#considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00
#informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros
#comprar apenas galões de 3,6 litros
#misturar latas e galões, de forma que o desperdício de tinta seja menor
#acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# para cada divisão : / )


import math #biblioteca para funções matemáticas 


área = float(input("digite a área em metros quadrados a ser pintada: "))
litros_necessários = área / 6 
litros_necessários_com_folga = litros_necessários * 1.1  #acrescentando 10% de folga
#situação 1: apenas latas de 18 litros
latas_18l = math.ceil(litros_necessários_com_folga / 18)

custo_latas_18l = latas_18l * 80.00 

#situação 2: apenas galões de 3,6 litros

galões_3_6l= math.ceil(litros_necessários_com_folga / 3.6)

custo_galões_3_6l = galões_3_6l * 25.00

#situação 3: mistura de latas e galões
latas_mistas = math.floor(litros_necessários_com_folga / 18)
litros_restantes = litros_necessários_com_folga - (latas_mistas * 18)
galões_mistura = math.ceil(litros_restantes / 3.6) 

custo_misto = (latas_mistas * 80.00) + (galões_mistura * 25.00) 

print (f"\nsituação 1: apenas latas de 18 litros")
print (f"quantidade de latas necessárias: {latas_18l}")
print (f"custo total: R$ {custo_latas_18l:.2f}") 
print (f"\nsituação 2: apenas galões de 3,6 litros")
print (f"quantidade de galões necessárias: {galões_3_6l}")
print (f"custo total: R$ {custo_galões_3_6l:.2f}")
print (f"\nsituação 3: mistura de latas e galões")
print (f"quantidade de latas necessárias: {latas_mistas}")
print (f"quantidade de galões necessárias: {galões_mistura}")      
print (f"custo total: R$ {custo_misto:.2f}")

      