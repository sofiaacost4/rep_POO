import streamlit as st
from views import View
import pandas as pd
import time

class ConfirmarServicoUI:
    def main():
        dic = []
        st.header("Confirmar Serviço")
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum serviço cadastrado para você")
        else: 
            for obj in horarios:
                if obj.get_id_profissional() == st.session_state["usuario_id"]:
                        horario = st.selectbox("Informe o horário", horarios)
                profissionais = View.profissional_listar()
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                if cliente != None: cliente = cliente.get_nome()
                cliente = st.selectbox("Cliente", cliente)
                if st.button("Confirmar"):
                    View.horario_atualizar(horario.get_id(),
                        horario.get_data(), False,
                        st.session_state["usuario_id"],
                        cliente.get_id(), horario.get_id())
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()


