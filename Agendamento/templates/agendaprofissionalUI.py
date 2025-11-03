import streamlit as st
from views import View
import time
from datetime import datetime

class AgendaProfissionalUI:
    def main():
        st.header("Abrir Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        h_i = st.text_input("Informe o horário inicial no formato HH:MM")
        h_f = st.text_input("Informe o horário final no formato HH:MM")
        i = st.text_input("Digite o intervalo de tempo entre os horários (min):", "")
        if st.button("Abrir Agenda"):
            try:
                View.profissional_agenda(data, h_i, h_f, int(i),(st.session_state["usuario_id"]))
                st.success("Agenda inserida com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))