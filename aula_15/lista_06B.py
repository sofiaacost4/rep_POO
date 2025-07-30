import json
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
    def p_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "nasc": self.__nasc.strftime("%d/%m/%Y")
        }
    @staticmethod
    def de_dict(d):
        dt_nasc = datetime.strptime(d["nasc"], "%d/%m/%Y")
        return Contato(d["id"], d["nome"], d["email"], d["fone"], dt_nasc)
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc}"

class ContatoUI:
    __contatos = []
    __an = []
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniversariantes()
            if op == 8: ContatoUI.abrir()
            if op == 9: ContatoUI.salvar()
    @staticmethod
    def menu():
        print("1 - Inserir | 2 - Listar | 3 - Listar ID | 4 - Atualizar | 5 - Excluir | 6 - Pesquisar | 7 - Aniversariantes | 8 - Abrir | 9 - Salvar | 10 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def inserir():
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome do contato: ")
        email = input("Informe o email do contato: ")
        fone = input("Informe o telefone do contato: ")
        nasc = input("(dd/mm/aaaa) <- Informe a data de nascimento: ")
        dt_nasc = datetime.strptime(nasc, "%d/%m/%Y")
        C = Contato(id, nome, email, fone, dt_nasc)
        ContatoUI.__contatos.append(C)
    @staticmethod
    def listar():
        for c in ContatoUI.__contatos:
            print(c)
    @staticmethod
    def listar_id():
        id = int(input("Qual é o ID que você deseja listar? "))
        for c in ContatoUI.__contatos:
            if c.get_id() == id: print(c)
            else: print("Id não encontrado.")
    @staticmethod
    def atualizar():
        id = int(input("Qual é o ID que você deseja atualizar? "))
        for c in ContatoUI.__contatos:
            if c.get_id() == id:
                print(c)
                n_id = int(input("Informe o novo id do contato: "))
                nome = input("Informe o novo nome do contato: ")
                email = input("Informe o novo email do contato: ")
                fone = input("Informe o novo telefone do contato: ")
                nasc = input("(dd/mm/aaaa) <- Informe a nova data de nascimento: ")
                dt_nasc = datetime.strptime(nasc, "%d/%m/%Y")
                i = Contato(n_id, nome, email, fone, dt_nasc)
                ContatoUI.__contatos.append(i)
                ContatoUI.__contatos.remove(c)
                break
        else:
            print("Contato com esse ID não foi encontrado.")
    @staticmethod
    def excluir():
        ContatoUI.listar()
        id = int(input("Qual é o id do contato que você deseja excluir? "))
        for i in ContatoUI.__contatos:
            if i.get_id() == id:
                ContatoUI.__contatos.remove(i)
    @staticmethod
    def pesquisar():
        nome = input("Informe o nome:")
        for c in ContatoUI.__contatos:
            if c.get_nome().startswith(nome): print(c)
    @staticmethod
    def aniversariantes():
        m = int(input("Qual é o mês que deseja saber os aniversariantes? "))
        ContatoUI.__an = [c.get_nome() for c in ContatoUI.__contatos if c.get_nasc().month == m]
        if ContatoUI.__an:
            print("Aniversariantes:")
            for nome in ContatoUI.__an:
                print(nome)
        else:
            print("Nenhum aniversariante neste mês.")
    @staticmethod
    def abrir():
        x = []
        with open("contatos.json", mode="r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
            for dic in lista:
                c = Contato.de_dict(dic)
                x.append(c)
        for c in x:
            print(c)
    @staticmethod
    def salvar():
        dados = [c.p_dict() for c in ContatoUI.__contatos]
        with open("contatos.json", mode ="w") as arq:
            json.dump(dados, arq, default = vars)
        print("Contatos salvos com sucesso.")

ContatoUI.main()