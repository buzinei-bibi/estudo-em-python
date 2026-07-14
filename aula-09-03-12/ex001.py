# classe pessoa - cadastro e rotinas diárias

# situação
# você está criando um módulo de cadastro
# para um aplicativo de saúde e bem-estar,
# que precisa armazenar informações de pessoas e
# simular algumas ações do dia a dia.

# requisitos
# crie uma classe chamada pessoa com os atributos:
# nome, idade, altura (em metros), peso (em kg) e métodos:
# apresentar() - imprime uma apresentação da pessoa
# envelhecer() - aumenta a idade em +1
# engordar(valor) - aumenta o peso
# emagrecer(valor) - diminui o peso
# calcular_imc() - retorna o IMC da pessoa
# status_saude() - baseado no IMC, retorna:
#   < 18.5 "abaixo do peso"
#   18.5 - 24.9 "peso normal"
#   25 - 29.9 "sobrepeso"
#   >= 30 "obesidade"

class pessoa:
    def _init_(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def apresentar(self):
        print(f"olá, meu nome é {self.nome}, tenho {self.idade} anos, "
              f"{self.altura:.2f}m de altura e peso {self.peso}kg.")

    def envelhecer(self):
        self.idade += 1

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        self.peso -= valor

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def status_saude(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "abaixo do peso"
        elif 18.5 <= imc <= 24.9:
            return "peso normal"
        elif 25 <= imc <= 29.9:
            return "sobrepeso"
        else:
            return "obesidade"

    # desafio extra
    def crescer(self, cm):
        if self.idade < 21:
            self.altura += cm / 100  # cm → metros


# --------- TAREFA ---------

# 1) criar uma pessoa
p1 = pessoa("bianca", 19, 1.65, 64)

# 2) simular ela engordando 2kg, depois emagrecendo 1kg
p1.engordar(2)
p1.emagrecer(1)

# 3) mostrar IMC e status
print(f"IMC: {p1.calcular_imc():.2f}")
print("status de saúde:", p1.status_saude())

# 4) simular envelhecer 3 anos
for _ in range(3):
    p1.envelhecer()

# 5) usar o método crescer (somente se <21 anos)
p1.crescer(2)  # só cresce se ainda tiver menos de 21

# mostrar apresentação final
p1.apresentar()
