import streamlit as st
from views import View
import pandas as pd
import time

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")
        horarios = View.horario_listar()

        if len(horarios) == 0:
            st.write("Nenhum serviço cadastrado para você")
            return  # sai da função

        # Mostra todos os horários disponíveis no selectbox (fora do loop)
        opcoes = []
        for h in horarios:
            profissional = View.profissional_listar_id(h.get_id_profissional())
            servico = View.servico_listar_id(h.get_id_servico())
            nome_prof = profissional.get_nome() if profissional else "Desconhecido"
            nome_serv = servico.get_descricao() if servico else "Serviço não definido"
            opcoes.append(f"{h.get_data().strftime('%d/%m/%Y %H:%M')} - {nome_prof} ({nome_serv})")

        # Selectbox único, com key única
        escolha = st.selectbox("Informe o horário", opcoes, key="confirmar_horario")

        # Encontra o objeto correspondente à escolha
        horario = horarios[opcoes.index(escolha)]

        # Mostra o cliente correspondente, se existir
        cliente = None
        for c in View.cliente_listar():
            if c.get_id() == horario.get_id_cliente():
                cliente = c
                break

        if cliente:
            st.write(f"Cliente: {cliente.get_nome()}")

        # Botão para confirmar
        if st.button("Confirmar", key="btn_confirmar"):
            View.horario_atualizar(
                horario.get_id(),
                horario.get_data(),
                True,
                cliente.get_id() if cliente else None,
                horario.get_id_servico(),
                horario.get_id_profissional()
            )
            st.success("Horário agendado com sucesso!")
            time.sleep(2)
            st.rerun()
