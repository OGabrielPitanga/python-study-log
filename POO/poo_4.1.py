class Player:
    def __init__(self, nome, level):
        self.nome = nome
        self.level = level
    
class PlayerClass(Player):
    def __init__(self, nome, level, classe):
        super().__init__(nome, level)
        self.classe = classe

    def status(self):
        print(f"Nome: {self.nome} | Level : {self.level} | Classe: {self.classe}\n")

def selecionar_classe():
    classes_dict = {
        1: "Guerreiro",
        2: "Mago",
        3: "Ladino",
        4: "Clérigo",
        5: "Druida\n"
    }

    print("\nEscolha sua classe: ")
    for key, value in classes_dict.items():
        print(f"{key} - {value}")

    try:
        escolha = int(input("Escolha: "))
        return classes_dict[escolha]
    except (ValueError, KeyError):
        print("Escolha inválida -> Classe padrão: Guerreiro")
        return "Guerreiro"
    
# --- Entrada de dados --- #

nome_input = input("Digite o nome do jogador: ")

try:
    level_input = int(input("Digite o level do jogador: "))
except ValueError:
    print(f"Level inválido! Uando level 1 por padrão.")
    level_input = 1

classe_input = selecionar_classe()
jogador = PlayerClass(nome_input, level_input, classe_input)

print("\nInformações do jogador: ")
jogador.status()