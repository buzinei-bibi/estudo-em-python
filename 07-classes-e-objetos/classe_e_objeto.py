#programação orientada a objetos - classes e objetos 
class carro: #nome da classe
     
        #atributo de características:
        marca = ""
        modelo = ""
        ano = 0

        #construir (inicializar) os atributos (características)
        def _init_(self, marca, modelo, ano):

            self.marca = marca
            self.modelo = modelo
            self.ano = ano

    #métodos (ações)
def apresentar_carro(self):
        return f"carro: {self.marca} , {self.modelo} , ano: {self.ano}"

#chamar os objetos
carro1= carro ("toyota" , "corolla" , 2020)
carro2= carro ("honda" , "civic" , 2019)

print(carro1.apresentar_carro()) 

