from views import View
from datetime import datetime

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 8:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.listar_id()
            if op == 4: UI.atualizar()
            if op == 5: UI.excluir()
            if op == 6: UI.pesquisar()
            if op == 7: UI.aniversariantes()

    @staticmethod
    def menu():
        return int(input(" 1 - Inserir\n 2 - Listar\n 3 - Listar ID\n 4 - Atualizar\n 5 - Excluir\n 6 - Pesquisar\n 7 - Aniversariantes\n 8 - Fim\n Escolha uma opção: "))

    @staticmethod    
    def listar():
        for contato in View.contato_listar():
            print(contato)

    @staticmethod    
    def listar_id():
        id = int(input("Insira o id: "))
        c = View.contato_listar_id(id)
        if c: 
            print(c)
        else: 
            print("Contato não encontrado.")

    @staticmethod 
    def inserir():
        nome = input("Informe o nome do contato: ")
        email = input("Informe o email do contato: ")
        fone = input("Informe o telefone do contato: ")
        dn = datetime.strptime(input("Data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        View.contato_inserir(nome, email, fone, dn)
        print("Contato inserido com sucesso.")

    @staticmethod
    def atualizar():
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o novo nome do contato: ")
        email = input("Informe o novo email do contato: ")
        fone = input("Informe o novo telefone do contato: ")
        dn = datetime.strptime(input("Informe a nova data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        View.contato_atualizar(id, nome, email, fone, dn)
        print("Dados alterados com sucesso.")

    @staticmethod
    def excluir():
        id = int(input("Informe o id do contato: "))
        View.contato_excluir(id)
        print("Dados excluídos com sucesso.")

    @staticmethod
    def pesquisar():
        nome = input("Insira o nome: ")
        n = View.contato_pesquisar(nome)
        print(n)

    @staticmethod
    def aniversariantes():
        mes = int(input("Insira o mês do aniversariante: "))
        r = View.contato_aniversariantes(mes)
        print(r)


UI.main()
