class Carro:
    def ligar(self):
        print("O carro ligar")
    
class Civic(Carro):
    def ligar(self):
        print("O Civic ligou")

class Gol(Carro):
    def ligar(self):
        print("O Gol ligou")

# Usando polimorfismo:
def fazer_carro_ligar(carro):
    carro.ligar()

# Teste
carros = [Civic(), Gol(), Carro()]

for a in carros:
    fazer_carro_ligar(a)

# -> um mesmo método, comportamentos diferentes.