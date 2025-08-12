from lista_07B import Contato, ContatoDAO

class View:
    @staticmethod
    def contato_listar():
        return ContatoDAO.listar()

    @staticmethod
    def contato_listar_id(id):
        return ContatoDAO.listar_id(id)

    @staticmethod
    def contato_inserir(nome, email, fone, dn):
        return ContatoDAO.inserir(Contato(0, nome, email, fone, dn))

    @staticmethod
    def contato_atualizar(id, nome, email, fone, dn):
        return ContatoDAO.atualizar(Contato(id, nome, email, fone, dn))

    @staticmethod
    def contato_excluir(id):
        return ContatoDAO.excluir(id)

    @staticmethod
    def contato_aniversariantes(mes):
        return ContatoDAO.aniversariantes(mes)

    @staticmethod
    def contato_pesquisar(nome):
        return ContatoDAO.pesquisar(nome)
