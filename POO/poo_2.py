class PickNum:
    def __init__(self, num):
        self.num = num
        self.par_impar()

    def par_impar(self):
        if self.num % 2 == 0:
            self.parimpar = "Par"
        else:
            self.parimpar = "Impar"

    def show_num(self):
        print(f"numero = {self.num}, é: {self.parimpar}")


picked_num = PickNum(2)
picked_num.show_num()
