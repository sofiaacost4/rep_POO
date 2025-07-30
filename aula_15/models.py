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

class ContatoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.__abrir() 
        id = 0
        for aux in cls.__objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1   
        cls.__objetos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()    
        return cls.__objetos

    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Contato(dic["id"], dic["nome"])
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass             

    @classmethod
    def __salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = vars)
