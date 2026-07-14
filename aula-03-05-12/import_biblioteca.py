#importação de bibliotecas e função

import time
import random
import math

numero_raiz = math.sqrt(25)
print(numero_raiz)

def gerar_numero_aleatorio():
    numero = random.randint(1,10)
    return numero

print(gerar_numero_aleatorio())