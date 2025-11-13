import streamlit as st
from views import View
import time

class ConfirmarPagamentoUI:
    def main():
        st.header("Confirmar Pagamento")
        id_cliente = st.session_state["usuario_id"]
        horarios = View.horario_ver_servicos(id_cliente)
        if not horarios:
            st.write("Nenhum serviço agendado.")
            return
        opcoes = []
        for h in horarios:
            servico = View.servico_listar_id(h.get_id_servico())
            pagamento = View.pagamento_listar_por_horario(h.get_id())
            estado_pag = pagamento.get_estado() if pagamento else "Pendente"
            if estado_pag == "Pendente":
                opcoes.append(f"{h.get_data().strftime('%d/%m/%Y %H:%M')} - {servico.get_descricao()} ({estado_pag})")
        escolha = st.selectbox("Selecione o serviço", opcoes)
        horario_escolhido = horarios[opcoes.index(escolha)]
        servico = View.servico_listar_id(horario_escolhido.get_id_servico())
        valor_total = servico.get_valor()
        max_parcelas = servico.get_parcelas()
        st.write(f"Valor total: R$ {valor_total:.2f}")
        st.write(f"Parcelamento: até {max_parcelas}x")
        max_parcelas = int(servico.get_parcelas())
        parcelas_escolhidas = st.slider("Escolha o número de parcelas", 1, max_parcelas, 1)
        valor_parcela = valor_total / parcelas_escolhidas
        st.info(f"Você pagará {parcelas_escolhidas}x de R$ {valor_parcela:.2f}")
        if st.button("Confirmar Pagamento"):
            try:
                p = View.pagamento_confirmar(horario_escolhido.get_id(), parcelas_escolhidas)
                st.success(f"Pagamento {p.get_estado()} com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
