class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def get_id(self):
        return self.__id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        else: self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_email(self, email):
        if email == "": raise ValueError()
        else: self.__email = email
    def get_email(self):
        return self.__email
