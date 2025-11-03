import streamlit as st
from views import View
import time
from datetime import datetime

class AgendaProfissionalUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        h_inicial = st.text_input("Informe o horário inicial no formato HH:MM")
        h_final = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (mins)")
        if st.button("Abrir Agenda"):
            View.profissional_agenda(data, h_inicial, h_final, int(intervalo), st.session_state["usuario_id"])
            st.success("Agenda criada com sucesso")
            time.sleep(2)
            st.rerun()
