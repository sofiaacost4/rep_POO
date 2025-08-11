from views import View

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.listar()
            if op == 2: UI.inserir()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    @staticmethod
    def menu():
        return int(input(" 1 - Listar\n 2 - Inserir\n 3 - Atualizar\n 4 - Excluir\n 5 - Fim\nEscolha uma opção: "))
    @staticmethod    
    def listar():
        for cliente in View.cliente_listar():
            print(cliente)
    @staticmethod 
    def inserir():
        nome = input("Informe o nome do cliente: ")
        email = input("Informe o email do cliente: ")
        fone = input("Informe o telefone do cliente: ")
        View.cliente_inserir(nome, email, fone)
        print("Cliente inserido com sucesso")
    @staticmethod
    def atualizar():
        id = int(input("Informe o id do cliente: "))
        nome = input("Informe o novo nome do cliente: ")
        email = input("Informe o novo email do cliente: ")
        fone = input("Informe o novo telefone do cliente: ")
        View.cliente_atualizar(id, nome, email, fone)
        print("Dados alterados com sucesso.")
    @staticmethod
    def excluir():
        id = int(input("Informe o id do cliente: "))
        View.cliente_excluir(id)
        print("Dados excluídos com sucesso.")
        

UI.main()