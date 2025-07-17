from datetime import datetime,timedelta
class Cinema:
    def __init__(self, n, i, d):
        self.set_nome(n)
        self.set_inicio(i)
        self.set_duracao(d)
    def set_nome(self, n):
        if n == "": raise ValueError()
        else: self.__nome = n
    def get_nome(self):
        return self.__nome
    def set_inicio(self, i):
        if i > datetime.now(): raise ValueError()
        else: self.__inicio = i
    def get_inicio(self):
        return self.__inicio
    def set_duracao(self, d):
        if d < timedelta(0): raise ValueError()
        else: self.__duracao = d
    def get_duracao(self):
        return self.__duracao
    def fim(self):
        return (self.__duracao + self.__inicio)
    def __str__(self):
        return f"Nome do filme: {self.__nome} | Data de início: {self.__inicio} | Duração do filme : {self.__duracao} | Fim: {Cinema.fim(self)}"

class CinemaUI:
    __sessoes = []
    @classmethod
    def main(cls):
        op = 0 
        while op != 4:
            op = CinemaUI.menu()
            if op == 1: CinemaUI.inserir()
            if op == 2: CinemaUI.listar()
            if op == 3: CinemaUI.calcular()
    @classmethod
    def menu(cls):
        print("1 - Inserir | 2 - Listar | 3 - Calcular | 4 - Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        n = input("Nome do filme: ")
        i = input("Data de início: ")
        i_n = datetime.strptime(i, "%d/%m/%Y %H:%M")
        d = input("Duração do filme (hh:mm): ")
        h, m = map(int, d.split(":"))
        d_n = timedelta(hours = h, minutes = m)
        c = Cinema(n, i_n, d_n)
        cls.__sessoes.append(c)
    @classmethod
    def listar(cls):
        if len(cls.__sessoes) == 0: print("Nenhuma sessão cadastrada.")
        else:
            for c in cls.__sessoes:
                print(c)
    @classmethod
    def calcular(cls):
        m_d = cls.__sessoes[0]
        for c in cls.__sessoes:
            if c.get_duracao() > m_d.get_duracao():
                m_d = c
        print(f"Sessão de maior duração: {m_d}")

CinemaUI.main()
