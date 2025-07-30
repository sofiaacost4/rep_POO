from models import Contato, ContatoDAO

class View:
    @staticmethod
    def contato_inserir(nome):
        ContatoDAO.inserir(Contato(0, nome))

    @staticmethod
    def contato_listar():
        return ContatoDAO.listar()
    