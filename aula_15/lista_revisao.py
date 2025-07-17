from datetime import datetime, timedelta
class Treino:
    def __init__(self, id, dt, ds, t):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_data(self, dt):
        if dt < 0: raise ValueError()
        self.__data = dt
    def set_distancia(self, ds):
        if ds < 0: raise ValueError()
        self.__distancia = ds
    def set_tempo(self, t):
        if t < 0: raise ValueError()
        t = self.__tempo
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def fim(self):
        return (self.__distancia / self.__tempo)
    def __str__(self):
        return f"Id: {self.__id}\nData: {self.__data}\nDistância: {self.__distancia}\nTempo: {self.__tempo}"

class TreinoUI:
    __treinos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.maisrapido()
    @classmethod
    def menu(cls):
        print("1 - Inserir | 2 - Listar | 3 - Listar ID | 4 - Atualizar | 5 - Excluir | 6 - Mais Rápido | 7 - Fim ")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Id: "))
        dt = input("(dd/mm/aaaa) <- Data do treino: ")
        dt_n = datetime.strptime(dt, "%d/%m/%Y")
        ds = int(input("Distância percorrida (em metros): "))
        t = input("(hh:mm:ss) <- Tempo da corrida: ")
        h, m, s = map(int, t.split(":"))
        t_n = timedelta(hours = h, minutes = m, seconds = s )
        treino = Treino(id, dt_n, ds, t_n)
        cls.__treinos.append(treino)
    @classmethod
    def listar(cls):
        for t in cls.__treinos:
            print(t)
    @classmethod
    def listar_id(cls):
        id = int(input("Qual é o id que deseja saber o treino? "))
        for i in cls.__treinos:
            if i.get_id() == id:
                print(i)
            else: print("Id não encontrado.")
    @classmethod
    def atualizar(cls):
        id = int(input("Qual é o id do treino que você deseja atualizar? "))
        for i in cls.__treinos:
            if i.get_id() == id:
                print(i)
                data = input("(dd/mm/aaaa) <- Data do treino atualizada: ")
                dt_a = datetime.strptime(data, "%d/%m/%Y")
                ds = int(input("Distância atualizada (em metros): "))
                tempo = input("(hh:mm:ss) <- Tempo atualizado: ")
                h, m, s = map(int, tempo.split(":"))
                t_at = timedelta(hours = h, minutes = m, seconds = s)
                y = Treino(id, dt_a, ds, t_at)
                cls.__treinos.remove(i)
                cls.__treinos.append(y)
                break
        else:
            print("Treino com esse ID não foi encontrado.")
    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Qual é o id do treino que você deseja excluir? "))
        for i in cls.__treinos:
            if i.get_id() == id:
                cls.__treinos.remove(i)
    @classmethod
    def maisrapido(cls):
        m_r = cls.__treinos[0]
        for t in cls.__treinos:
            if t.vel_media() > m_r.vel_media():
                m_r = t 
        print(t)
            

TreinoUI.main()