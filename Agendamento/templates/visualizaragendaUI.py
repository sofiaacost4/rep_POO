import streamlit as st
import pandas as pd
from views import View

class VisualizarAgendaUI:
    def main():
        dic = []
        st.header("Minha Agenda")
        horarios = View.horario_listar()
        for obj in horarios:
            cliente = View.cliente_listar_id(obj.get_id_cliente())
            servico = View.servico_listar_id(obj.get_id_servico())
            profissional = View.profissional_listar_id(obj.get_id_profissional())
            estado_pagamento = View.pagamento_listar_por_horario(obj.get_id())
            if cliente != None: cliente = cliente.get_nome()
            if servico != None: servico = servico.get_descricao()
            if profissional != None: profissional = profissional.get_nome()
            if estado_pagamento != None: estado_pagamento = estado_pagamento.get_estado()
            else: estado_pagamento = "Pendente"
            if obj.get_id_profissional() == (st.session_state["usuario_id"]):

                dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "serviço" : servico, "pagamento" : estado_pagamento})
        if dic:
            df = pd.DataFrame(dic)
            st.dataframe(df)

