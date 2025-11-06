from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from models.pagamento import Pagamento, PagamentoDAO
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
        try:
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
        except ValueError as erro:
            raise erro
    def cliente_atualizar(id, nome, email, fone, senha):
        try:
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
        except ValueError as erro:
            raise ValueError(erro)
    def cliente_excluir(id):
        try:
            for h in View.horario_listar():
                    if h.get_id_cliente() == id:
                        raise ValueError("Esse cliente não pode ser excluído, pois tem horário(s) cadastrado(s).")
            ClienteDAO.excluir(id)
        except ValueError as erro:
            raise ValueError(erro)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def cliente_alterar_admin(senha):
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                View.cliente_atualizar(c.get_id(),"admin", "admin", "fone", senha)
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_inserir(descricao, valor, parcelas):
        servico = Servico(0, descricao, valor, parcelas)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor, parcelas):
        servico = Servico(id, descricao, valor, parcelas)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", 0, 1)
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key=lambda h: h.get_data())
        return r

    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)

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
        horarios_cliente = View.horario_ver_servicos(id_cliente)
        for h1 in View.horario_listar():
            if h1.get_id() != id and h1.get_data() == data and h1.get_id_profissional() == id_profissional:
                raise ValueError("Esta data já está cadastrada na agenda desse profissional.")
        for h2 in horarios_cliente:
                if data == h2.get_data(): raise ValueError("Você já tem um horário agendado nessa data.")
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
    def horarios_para_confirmar(id_profissional):
        dic = []
        for h in View.horario_listar():
            if (h.get_id_profissional() == id_profissional and 
                not h.get_confirmado() and 
                h.get_id_cliente() != None):
                cliente = ClienteDAO.listar_id(h.get_id_cliente())
                servico = ServicoDAO.listar_id(h.get_id_servico())
                dic.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%d/%m/%Y %H:%M"),
                    "cliente": cliente.get_nome() if cliente else None,
                    "servico": servico.get_descricao() if servico else None})
        return dic
    def confirmar_horario(id_horario):
        h = View.horario_listar_id(id_horario)
        if not h:
            return False
        pagamento = View.pagamento_listar_por_horario(h.get_id())
        estado_pagamento = pagamento.get_estado() if pagamento else "Pendente"
        if estado_pagamento is None or estado_pagamento == "Pendente":
            raise ValueError("Pagamento pendente. O profissional não pode confirmar o serviço.")

        h.set_confirmado(True)
        View.horario_atualizar(
            h.get_id(),
            h.get_data(),
            h.get_confirmado(),
            h.get_id_cliente(),
            h.get_id_servico(),
            h.get_id_profissional()
        )
        return True

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_listar_profissionais():
        return ProfissionalDAO.listar_profissionais()
    def profissional_inserir(nome, email, especialidade, conselho, senha):
        try:
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
        except ValueError as erro:
            raise erro
    def profissional_atualizar(id, nome, email, especialidade, conselho, senha):
        try:
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
        except ValueError as erro:
            raise ValueError(erro)
    def profissional_excluir(id):
        try:
            for h in View.horario_listar():
                    if h.get_id_profissional() == id:
                        raise ValueError("Esse profissional não pode ser excluído, pois tem horário(s) cadastrado(s).")
            ProfissionalDAO.excluir(id)
        except ValueError as erro:
            raise ValueError(erro)
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
    from models.pagamento import Pagamento, PagamentoDAO


    def pagamento_confirmar(id_horario, parcelas_escolhidas):
        h = View.horario_listar_id(id_horario)
        servico = View.servico_listar_id(h.get_id_servico())
        valor_total = servico.get_valor()
        parcelas_totais = servico.get_parcelas()
        pagamento_existente = PagamentoDAO.listar_por_horario(id_horario)
        if pagamento_existente is None:
            valor_parcela = valor_total / parcelas_escolhidas
            p = Pagamento(0, id_horario, valor_total, parcelas_totais, parcelas_escolhidas, 1, valor_parcela, 
                          "Pago" if parcelas_escolhidas == 1 else "Pago parcialmente")
            PagamentoDAO.inserir(p)
            return p
        else:
            pagamento_existente.pagar_parcela()
            PagamentoDAO.atualizar(pagamento_existente)
            return pagamento_existente
    def pagamento_listar_por_horario(id_horario):
        p = PagamentoDAO.listar_por_horario(id_horario)
        if p:
            if p.atualizar_parcelas():
                PagamentoDAO.atualizar(p)
        return p
    def pagamentos_atualizar_todos():
        pagamentos = PagamentoDAO.listar()
        houve_atualizacao = False

        for p in pagamentos:
            if p.atualizar_parcelas():
                PagamentoDAO.atualizar(p)
                houve_atualizacao = True

        if houve_atualizacao:
            PagamentoDAO.salvar()




