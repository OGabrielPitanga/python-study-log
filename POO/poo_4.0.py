# Herança

class Player:  # Classe Base
    def __init__(self, nome, level):
        self.nome = nome
        self.level = level

    def status(self):
        print(f"Nome: {self.nome}| Level: {self.level}")


class PlayerClass(Player):  # Classe devivada (que herda da classe base "Player")
    def __init__(self, nome, level, classe):
        super().__init__(nome, level)
        self.classe = classe

    def show_class(self):
        print(f"Classe: {self.classe}")


# Entrada de dados:

nome_input = input("Digite o nome do jogador: ")
level_input = input("Digite o level do jogador: ")
classe_input = input("Digite a classe do jogador: ")

# Validação simples (Convertendo level para inteiro)
try:
    level_input = int(level_input)
except ValueError:
    print("Level invalido -> Usando level 1 por padrão")
    level_input = 1

jogador = PlayerClass(nome_input, level_input, classe_input)

print("\n Informações do jogador:")
jogador.status()
jogador.show_class()
