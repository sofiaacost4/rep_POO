class Profissional:
    def __init__(self, id, nome, email, especialidade, conselho, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_senha(senha)

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_especialidade(self):
        return self.__especialidade
    def get_conselho(self):
        return self.__conselho
    def get_senha(self):
        return self.__senha
    
    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        else: self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError()
        else: self.__email = email
    def set_especialidade(self, especialidade):
        if especialidade == "": raise ValueError()
        else: self.__especialidade = especialidade
    def set_conselho(self, conselho):
        if conselho == "": raise ValueError()
        else: self.__conselho = conselho
    def set_senha(self, senha):
        if senha == "": raise ValueError()
        else: self.__senha = senha


    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade} - {self.__conselho} - {self.__senha}"
    
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email": self.__email, "especialidade": self.__especialidade, "conselho": self.__conselho, "senha": self.__senha}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"],dic["nome"],dic["email"],dic["especialidade"],dic["conselho"],dic["senha"])

import json

class ProfissionalDAO():
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    @classmethod
    def listar_profissionais(cls):
        cls.abrir()
        cls.__objetos_listados = [
            Profissional(p.get_id(), p.get_nome(), p.get_email(), p.get_especialidade(), p.get_conselho(), senha="*")
            for p in cls.__objetos
        ]
        return cls.__objetos_listados
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass 

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Profissional.to_json)
                
