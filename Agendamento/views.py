from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime
from datetime import timedelta

class View:
        
    def cliente_listar():
        r =  ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def cliente_listar_objetos():
        return ClienteDAO.listar_clientes()
    def cliente_inserir(nome, email, fone, senha):
        for c in View.cliente_listar():
            if email == "admin":
                raise ValueError("Você não pode inserir um admin.")
            if c.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
        for p in View.profissional_listar():
            if p.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        for c in View.cliente_listar():
            if email == "admin":
                raise ValueError("Você não pode atualizar um admin.")
            if c.get_id() != id:
                if c.get_email() == email:
                    raise ValueError("Este email já é utilizado por um usuário.")
        for p in View.profissional_listar():
            if p.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        for h in View.horario_listar():
                if h.get_id_cliente() == id:
                    raise ValueError("Esse cliente não pode ser excluído, pois tem horário(s) cadastrado(s).")
        ClienteDAO.excluir(id)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def horario_listar_id(id):
        horario =  HorarioDAO.listar_id(id)
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for h in View.horario_listar():
            if h.get_data() == data and h.get_id_profissional() == id_profissional:
                raise ValueError("Essa data já está cadastrada na agenda desse profissional.")
        h = Horario(0, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.inserir(h)
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        if data == None:
            raise ValueError("Data não pode ser vazio.")
        for h in View.horario_listar():
            if h.get_id() != id and h.get_data() == data and h.get_id_profissional() == id_profissional:
                raise ValueError("Esta data já está cadastrada na agenda desse profissional.")
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)
    def horario_excluir(id, data):
        for h in View.horario_listar():
            if h.get_data() != None and h.get_id_cliente() != None and h.get_id_servico() != None and h.get_id_profissional() != None:
                raise ValueError("Esse horário não pode ser excluído pois já foi agendado.")
        h = Horario(id, data)
        HorarioDAO.excluir(h)
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    def horario_ver_servicos(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_listar_profissionais():
        return ProfissionalDAO.listar_profissionais()
    def profissional_inserir(nome, email, especialidade, conselho, senha):
        for p in View.profissional_listar():
            if email == "admin":
                raise ValueError("Você não pode inserir um admin.")
            if p.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
        for c in View.cliente_listar():
            if c.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
        profissional = Profissional(0, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.inserir(profissional)
    def profissional_atualizar(id, nome, email, especialidade, conselho, senha):
        for p in View.profissional_listar():
            if email == "admin":
                raise ValueError("Você não pode atualizar um admin.")
            if p.get_id() != id:
                if p.get_email() == email:
                    raise ValueError("Este email já é utilizado por um usuário.")
        for c in View.cliente_listar():
            if c.get_email() == email:
                raise ValueError("Este email já é utilizado por um usuário.")
            profissional = Profissional(id, nome, email, especialidade, conselho, senha)
            ProfissionalDAO.atualizar(profissional)
    def profissional_excluir(id):
        for h in View.horario_listar():
                if h.get_id_profissional() == id:
                    raise ValueError("Esse profissional não pode ser excluído, pois tem horário(s) cadastrado(s).")
        ProfissionalDAO.excluir(id)
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id" : p.get_id(), "nome" : p.get_nome()}
        return None
    def profissional_agenda(data, h_i, h_f, i, id):
        primeiro_horario = datetime.strptime(data + " " + h_i, "%d/%m/%Y %H:%M")
        ultimo_horario = datetime.strptime(data + " " + h_f, "%d/%m/%Y %H:%M")
        intervalo_min = timedelta(minutes = i)
        x = primeiro_horario
        while x <= ultimo_horario:
            View.horario_inserir(x, False, None, None, id)
            x += intervalo_min




