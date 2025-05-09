class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property               ##@property: permite ler p.preco como se fosse um atributo.
    def preco(self):
        return self.__preco

    @preco.setter           ##@preco.setter: permite definir o valor com p.preco = valor.
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço inválido")


p = Produto("Notebook", 3000)
print(p.preco)

p.preco = 50
print(p.preco)