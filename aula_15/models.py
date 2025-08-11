import json
from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, na):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = na

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

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
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"


class ContatoDAO:
    __contatos = []
    @classmethod
    def inserir(cls, obj):
        cls.__abrir() 
        id = 0
        for aux in cls.__contatos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id = id + 1   
        cls.__objetos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()    
        return cls.__contatos
    
    @classmethod
    def buscar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def atualizar(cls, contato):
        for i, c in enumerate(cls.__contatos):
            if c.get_id() == contato.get_id():
                cls.__contatos[i] = contato
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.__contatos = [c for c in cls.__contatos if c.get_id() != id]

    @classmethod
    def pesquisar(cls, nome):
        return [c for c in cls.__contatos if c.get_nome().startswith(nome)]

    @classmethod
    def aniversariantes(cls, mes):
        return [c.get_nome() for c in cls.__contatos if c.get_nasc().month == mes]


    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["nasc"])
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass             

    @classmethod
    def __salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = vars)


