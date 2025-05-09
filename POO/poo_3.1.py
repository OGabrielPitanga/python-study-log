class Usuario:
    cargo = 'usuário'
    def __init__(self, nome, idade, altura):
        self.altura = altura
    
    def retorna_altura(self):
        print(self.altura)

    def exibe_cargo(cls):
        print(cls.cargo)
    
usuario1 = Usuario('gabriel', '19', '1,85')

usuario2 = Usuario('eduarda', '19', '1.57')

usuario1.exibe_cargo()
usuario2.exibe_cargo()
print('-----------')
usuario1.cargo = 'gerente'
usuario1.exibe_cargo()
usuario2.exibe_cargo()
print('-----------')
Usuario.cargo = 'gerente'
usuario1.exibe_cargo()
usuario2.exibe_cargo()