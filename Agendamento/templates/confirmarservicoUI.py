import streamlit as st
from views import View
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")
        id_profissional = st.session_state.get("usuario_id")
        horarios = View.horarios_para_confirmar(id_profissional)
        if not horarios:
            st.write("Nenhum serviço agendado para você.")
            return
        opcoes = [f"{h['data']} - {h['servico']}"
            for h in horarios]
        escolha = st.selectbox("Selecione o horário", opcoes)
        horario_escolhido = horarios[opcoes.index(escolha)]
        st.selectbox(f"Cliente:", {horario_escolhido['cliente']})
        if st.button("Confirmar"):
            try:
                View.confirmar_horario(horario_escolhido["id"])
                st.success("Horário confirmado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
