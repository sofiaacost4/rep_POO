class Pais:
    def __init__(self, i, n, p, a):
        self.__id = i
        self.__nome = n
        self.__pop = p
        self.__area = a
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_pop(self):
        return self.__pop
    def get_area(self):
        return self.__area
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__pop} - {self.__area}"

class PaisUI:
    __paises = []
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            if op == 2: PaisUI.listar()
            if op == 3: PaisUI.atualizar()
            if op == 4: PaisUI.excluir()
            if op == 5: PaisUI.maispopuloso()
            if op == 6: PaisUI.maispovoado()
    @classmethod
    def menu(cls):
        print("1 - Inserir | 2 - Listar | 3 - Atualizar | 4 - Excluir | 5 - Mais populoso | 6 - Mais povoado | 7 - Fim")
        return int(input("Escolha uma opção:"))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do país:"))
        nome = input("Informe o nome do país:")
        pop = int(input("Informe a população do país:"))
        area = int(input("Informe a área do país:"))
        P = Pais(id, nome, pop, area)
        cls.__paises.append(P)
    @classmethod
    def listar(cls):
        #print (cls.__paises)
        for p in cls.__paises:
            print(p)
    @classmethod
    def atualizar(cls):
        id = int(input("Qual é o id do país que você deseja atualizar? "))
        for i in cls.__paises:
            if i.get_id() == id:
                print(i)
                nome = input("Nome atualizado: ")
                pop = int(input("População atualizada: "))
                area = int(input("Área atualizada: "))
                y = Pais(id, nome, pop, area)
                cls.__paises.remove(i)
                cls.__paises.append(y)
                break
        else:
            print("País com esse ID não foi encontrado.")
            
    @classmethod
    def excluir(cls):
        id = int(input("Qual é o id do país que você deseja excluir? "))
        for i in cls.__paises:
            if i.get_id() == id:
                cls.__paises.remove(i)
    @classmethod
    def maispopuloso(cls):
        if not cls.__paises:
            print("Nenhum país cadastrado.")
            return
        maispop = cls.__paises[0]
        for p in cls.__paises[1:]:
            if p.get_pop() > maispop.get_pop():
                maispop = p
        print(f"País mais populoso: {maispop.get_nome()} ({maispop.get_pop()} habitantes)")

    @classmethod
    def maispovoado(cls):
        if not cls.__paises:
            print("Nenhum país cadastrado.")
            return
        maispov = cls.__paises[0]
        for p in cls.__paises[1:]:
            densidade_atual = p.get_pop() / p.get_area()
            densidade_maior = maispov.get_pop() / maispov.get_area()
            if densidade_atual > densidade_maior:
                maispov = p
        densidade = maispov.get_pop() / maispov.get_area()
        print(f"País mais povoado: {maispov.get_nome()} (densidade: {densidade:.2f} hab/km²)")

PaisUI.main()