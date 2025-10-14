import streamlit as st
from views import View
import time
from datetime import datetime
from datetime import timedelta

class AgendaProfissionalUI:
    def main():
        st.header("Abrir Agenda")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        h_i = st.text_input("Informe o horário inicial no formato HH:MM", datetime.now().strftime("%H:%M"))
        h_f = st.text_input("Informe o horário final no formato HH:MM", datetime.now().strftime("%H:%M"))
        i = st.text_input("Informe o intervalo de tempo entre os horários(min)", "0")
        if st.button("Abrir Agenda"):
            id = op.get_id()
            View.horario_inserir(datetime.strptime(data, "%d/%m/%Y"), False, None, None, id)
            st.success("Agenda inserida com sucesso")
