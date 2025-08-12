import json
from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, dn):
        self.__id = i 
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__dn = dn

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_nome(self): return self.__nome
    def set_nome(self, n):
        if n == "": raise ValueError()
        self.__nome = n
    def get_email(self): return self.__email
    def set_email(self, e):
        if e == "": raise ValueError()
        self.__email = e
    def get_fone(self): return self.__fone
    def set_fone(self, f):
        if f == "": raise ValueError()
        self.__fone = f
    def get_dn(self): return self.__dn
    def set_dn(self, dn):
        if dn > datetime.today(): raise ValueError()
        self.__dn = dn

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "dn" : datetime.strftime(self.__dn, "%d/%m/%Y")
        }

    @staticmethod
    def from_dict(d):
        return Contato(d["id"], d["nome"], d["email"], d["fone"], datetime.strptime(d["dn"], "%d/%m/%Y"))
        
    def __str__(self):
        return f"Id: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Telefone: {self.__fone} | Nascimento: {self.__dn.strftime("%d/%m/%Y")}"
        

class ContatoDAO:
    __contatos = []

    @classmethod
    def inserir(cls, obj):
        cls.__abrir() 
        id = 0
        for aux in cls.__contatos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)  
        cls.__contatos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__contatos

    @classmethod
    def listar_id(cls, id):
        cls.__abrir()
        for c in cls.__contatos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def atualizar(cls, contato):
        cls.__abrir()
        for i, c in enumerate(cls.__contatos):
            if c.get_id() == contato.get_id():
                cls.__contatos[i] = contato
                cls.__salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.__abrir()
        for i, c in enumerate(cls.__contatos):
            if c.get_id() == id:
                cls.__contatos.pop(i)
                cls.__salvar()
    @classmethod
    def pesquisar(cls, nome):
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)

    @classmethod
    def aniversariantes(cls, mes):
        cls.__abrir
        for c in cls.__contatos:
            if c.get_dn().month == mes:
                print(c.get_nome())
    @classmethod
    def __abrir(cls):
        cls.__contatos = []
        try: 
            with open("contatos.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], datetime.strptime(dic["dn"], "%d/%m/%Y"))
                    cls.__contatos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def __salvar(cls):
        lista = [obj.to_dict() for obj in cls.__contatos]
        with open("contatos.json", mode="w") as arquivo:
            json.dump(lista, arquivo, indent=4)
