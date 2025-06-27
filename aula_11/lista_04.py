class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    __contatos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
    @classmethod
    def menu(cls):
        print("1 - Inserir | 2 - Listar | 3 - Atualizar | 4 - Excluir | 5 - Pesquisar | 6 - Fim")
        return int(input("Escolha uma opção:"))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato:"))
        nome = input("Informe o nome do contato:")
        email = input("Informe o email do contato:")
        fone = input("Informe o telefone do contato:")
        C = Contato(id, nome, email, fone)
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
                y = Contato(id, nome, email, fone)
                cls.__contatos.remove(i)
                cls.__contatos.append(y)
                break
        else:
            print("Contato com esse ID não foi encontrado.")
            
    @classmethod
    def excluir(cls):
        pass
    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome:")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)

ContatoUI.main()