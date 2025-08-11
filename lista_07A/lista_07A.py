import json
class Cliente:
    def __init__(self, i, n, e, f):
        self.__id = i 
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def to_dict(self):
        return {
            "id" : self.__id,
            "nome" : self.__nome,
            "email" : self.__email,
            "fone" : self.__fone
            }

    @staticmethod
    def from_dict(d):
            return Cliente(d["id"], d["nome"], d["email"], d["fone"])
        
    def __str__(self):
            return f"Id: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Telefone: {self.__fone}"
        
class ClienteDAO:
    __objetos = []
    @classmethod
    def inserir(cls,obj):
        cls.__abrir() 
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)  
        cls.__objetos.append(obj)
        cls.__salvar()
    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__objetos
    @classmethod
    def listar_id(cls, id):
        cls.__abrir()
        for c in cls.__objetos:
            if c.get_id() == id:
                return c
        return None
    @classmethod
    def atualizar(cls, cliente):
        cls.__abrir()
        for i, c in enumerate(cls.__objetos):
            if c.get_id() == cliente.get_id():
                cls.__objetos[i] = cliente
                cls.__salvar()
                return True
        return False
    @classmethod
    def excluir(cls, id):
        cls.__abrir()
        for i, c in enumerate(cls.__objetos):
            if c.get_id() == id:
                cls.__objetos.pop(i)
                cls.__salvar()
    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Cliente(dic["id"], dic["nome"], dic.get("email",""), dic.get("fone",""))
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def __salvar(cls):
        lista = [obj.to_dict() for obj in cls.__objetos]
        with open("clientes.json", mode="w") as arquivo:
            json.dump(lista, arquivo, indent=4)



                                     




