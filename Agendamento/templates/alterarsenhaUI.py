import streamlit as st
from views import View
import time

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha")
        senha = st.text_input("Insira a nova senha")
        if st.button("Confirmar"):
            View.cliente_alterar_admin(senha)
            st.success("Senha alterada com sucesso")
            time.sleep(2)
            st.rerun()