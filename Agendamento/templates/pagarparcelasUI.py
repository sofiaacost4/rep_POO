import streamlit as st
from views import View
import time

class PagarParcelasUI:
    def main():
        st.header("Pagar Parcelas de Serviços")

        id_cliente = st.session_state["usuario_id"]
        horarios = View.horario_ver_servicos(id_cliente)

        if not horarios:
            st.write("Nenhum serviço agendado.")
            return

        opcoes = []
        pagamentos_existentes = []
        for h in horarios:
            pagamento = View.pagamento_listar_por_horario(h.get_id())
            if pagamento:
                servico = View.servico_listar_id(h.get_id_servico())
                info = f"{servico.get_descricao()} ({pagamento.get_parcelas_pagas()}/{pagamento.get_parcelas_escolhidas()} pagas)"
                opcoes.append(info)
                pagamentos_existentes.append(pagamento)

        if not opcoes:
            st.info("Você ainda não tem pagamentos para parcelar.")
            return

        escolha = st.selectbox("Selecione o pagamento para continuar", opcoes)
        pagamento = pagamentos_existentes[opcoes.index(escolha)]

        st.write(f" Valor total: R$ {pagamento.get_valor_total():.2f}")
        st.write(f" Parcelas pagas: {pagamento.get_parcelas_pagas()} / {pagamento.get_parcelas_escolhidas()}")
        st.write(f" Valor por parcela: R$ {pagamento.get_valor_parcela():.2f}")
        st.write(f" Estado atual: {pagamento.get_estado()}")

        if pagamento.get_estado() == "Pago":
            st.success("Este pagamento já está completamente quitado.")
            return

        if st.button("Pagar próxima parcela"):
            pagamento.pagar_parcela()
            from models.pagamento import PagamentoDAO
            PagamentoDAO.atualizar(pagamento)
            st.success(f"Parcela paga com sucesso! Agora {pagamento.get_parcelas_pagas()} / {pagamento.get_parcelas_escolhidas()}.")
            time.sleep(2)
            st.rerun()
