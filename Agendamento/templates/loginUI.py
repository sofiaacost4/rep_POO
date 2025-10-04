import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            p = View.profissional_autenticar(email, senha)
            c = View.cliente_autenticar(email, senha)
            if c == None and p == None: st.write("E-mail ou senha inválidos")
            elif c:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = "cliente" # pega o tipo de usuário que faz o login, nesse caso, cliente
                st.rerun()
            elif p:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["usuario_tipo"] = "profissional" # pega o tipo de usuário que faz o login, nesse caso, profissional
                st.rerun()


