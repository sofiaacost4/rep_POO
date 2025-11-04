from templates.manterservicoUI import ManterServicoUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.agendaprofissionalUI import AgendaProfissionalUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.visualizarservicosUI import VisualizarServicosUI
from templates.confirmarservicoUI import ConfirmarServicoUI
from templates.alterarsenhaUI import AlterarSenhaUI
from templates.confirmarpagamentoUI import ConfirmarPagamentoUI

from views import View
import streamlit as st

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Visualizar Serviços", "Agendar Serviço", "Confirmar Pagamento"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Visualizar Serviços": VisualizarServicosUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Confirmar Pagamento": ConfirmarPagamentoUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Agenda", "Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Agenda": AgendaProfissionalUI.main()
        if op == "Minha Agenda": VisualizarAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            cliente = st.session_state["usuario_tipo"] == "cliente"
            profissional = st.session_state["usuario_tipo"] == "profissional"
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            elif cliente: IndexUI.menu_cliente()
            elif profissional: IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    def main():
        View.cliente_criar_admin() #verifica se existe o usuário admin
        IndexUI.sidebar() # monta o sidebar

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
IndexUI.main()