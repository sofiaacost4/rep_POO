from datetime import datetime
class Contato:
    def __init__(self,i, n, e, f, na):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = na
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nasc(self):
        return self.__nasc
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc}"

class ContatoUI:
    __an = []
    __contatos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversariantes()
    @classmethod
    def menu(cls):
        print("1 - Inserir | 2 - Listar | 3 - Atualizar | 4 - Excluir | 5 - Pesquisar | 6 - Aniversariantes | 7 - Fim")
        return int(input("Escolha uma opção:"))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome do contato: ")
        email = input("Informe o email do contato: ")
        fone = input("Informe o telefone do contato: ")
        nasc = input("(dd/mm/aaaa) <- Informe a data de nascimento: ")
        dt_nasc = datetime.strptime(nasc, "%d/%m/%Y")
        C = Contato(id, nome, email, fone, dt_nasc)
        cls.__contatos.append(C)
    @classmethod
    def listar(cls):
        #print (cls.__contatos)
        for c in cls.__contatos:
            print(c)
    @classmethod
    def atualizar(cls):
        id = int(input("Qual é o id que você deseja atualizar? "))
        for i in cls.__contatos:
            if i.get_id() == id:
                print(i)
                nome = input("Nome atualizado: ")
                email = input("Email atualizado: ")
                fone = input("Telefone atualizado: ")
                nasc = input("(dd/mm/aaaa) <- Data de nascimento atualizada: ")
                dt_nasc = datetime.strptime(nasc, "%d/%m/%Y")
                y = Contato(id, nome, email, fone, dt_nasc)
                cls.__contatos.remove(i)
                cls.__contatos.append(y)
                break
        else:
            print("Contato com esse ID não foi encontrado.")
            
    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Qual é o id do contato que você deseja excluir? "))
        for i in cls.__contatos:
            if i.get_id() == id:
                cls.__contatos.remove(i)
    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome:")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)
    @classmethod
    def aniversariantes(cls):
        m = int(input("Qual é o mês que deseja saber os aniversariantes? "))
        for c in cls.__contatos:
            if m == c.get_nasc().month:
                cls.__an.append(c.get_nome())
        for c in cls.__an:
            print(c)
            cls.__an = []
ContatoUI.main()



