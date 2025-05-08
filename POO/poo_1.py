'''
Classe: é como um molde (ex: molde de bolo). Define atributos e comportamentos.
Objeto: é a instância da classe (ex: um bolo feito com o molde).
'''
class Cachorro:
    def latir(self):
        print("Au Au!")

meu_cachorro = Cachorro()  # objeto
meu_cachorro.latir()       # comportamento

'''
Abstração:
Esconder detalhes complexos e mostrar apenas o essencial.

Analogia: você dirige um carro sem saber como o motor funciona.
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        print(f"{self.nome} está falando")

