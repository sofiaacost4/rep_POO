import random
class Bingo:
    def __init__(self, num_bolas):
        self.__num_bolas = num_bolas
        if num_bolas < 5: raise ValueError("Num mínimo de bolas é 5.")
        self.__bolas = []
    def sortear(self):
        if len(self.__bolas) == self.__num_bolas:
            return -1
        s = random.randint(1, self.__num_bolas)
        while s in self.__bolas:
            s = random.randint(1, self.__num_bolas)
        self.__bolas.append(s)
        return s
    def sorteados(self):
        return sorted(self.__bolas)

class BingoUI:
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1: jogo = BingoUI.iniciar_jogo()
            if op == 2: BingoUI.sortear(jogo)
            if op == 3: BingoUI.sorteados(jogo)
    @staticmethod
    def menu():
        print("1 - Iniciar jogo | 2 - Sortear | 3 - Sorteados | 4 - Fim")
        return(int(input("Escolha uma opção: ")))
    @staticmethod
    def iniciar_jogo():
        jogo = Bingo(int(input("Informe o número de bolas: ")))
        return jogo
    @staticmethod
    def sortear(jogo):
        print(jogo.sortear())
    @staticmethod
    def sorteados(jogo):
        print(jogo.sorteados())

BingoUI.main()
