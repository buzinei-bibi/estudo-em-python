#clube de regatas do flamengo

class jogador: 
    def __init__(self, nome, posição, número):
        self.nome = nome
        self.posição = posição
        self.número = número
    def apresentar(self):
        return f"jogador: {self.nome}, posição: {self.posição}, número: {self.número}" 
jogador1 = jogador ("arrascaeta", "meio-campo", 10)
jogador2 = jogador ("danilo", "defensor", 5) 
print(jogador1.apresentar())
print(jogador2.apresentar())


class torcedor:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    def apresentar(self):
        return f"torcedor: {self.nome}, idade: {self.idade}, cidade: {self.cidade}"
torcedor= torcedor ("bianca", 18 , "xique-xique")
print(f"olá, eu sou a {torcedor.nome}, tenho {torcedor.idade} anos e moro em {torcedor.cidade}")


class rival:
    def __init__(self, nome, cidade, títulos):
        self.nome = nome
        self.cidade = cidade
        self.títulos = títulos
    def apresentar(self):
        return f"rival: {self.nome}, cidade: {self.cidade}, títulos: {self.títulos}"
rival1 = rival ("vasco", "rio de janeiro", 24)
rival2 = rival ("fluminense", "rio de janeiro", 31)
rival3 = rival ("botafogo", "rio de janeiro", 21)
print(rival1.apresentar())
print(rival2.apresentar())
print(rival3.apresentar())
