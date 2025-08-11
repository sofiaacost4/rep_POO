from lista_07A import Cliente, ClienteDAO

class View:
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()
    @staticmethod
    def cliente_inserir(nome, email, fone):
        return ClienteDAO.inserir(Cliente(0, nome, email, fone))
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        return ClienteDAO.atualizar(Cliente(id, nome, email, fone))
    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO.excluir(id)
    