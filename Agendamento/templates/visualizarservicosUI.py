import streamlit as st
from views import View
import pandas as pd

class VisualizarServicosUI:
    def main():
        st.header("Visualizar Serviços")
        dic = []

        # Atualiza automaticamente todos os pagamentos antes de mostrar
        View.pagamentos_atualizar_todos()

        horarios = View.horario_ver_servicos(st.session_state["usuario_id"])

        for obj in horarios:
            servico = View.servico_listar_id(obj.get_id_servico())
            profissional = View.profissional_listar_id(obj.get_id_profissional())
            pagamento = View.pagamento_listar_por_horario(obj.get_id())

            if pagamento:
                estado = pagamento.get_estado()
                pagas = pagamento.get_parcelas_pagas()
                total = pagamento.get_parcelas_escolhidas()
                valor_parcela = pagamento.get_valor_parcela()
                ultima = pagamento.get_data_ultima_parcela().strftime("%H:%M")
                info_pagamento = f"{estado} ({pagas}/{total}) - {total}x R${valor_parcela:.2f}"
            else:
                info_pagamento = "Pendente"

            dic.append({
                "id": obj.get_id(),
                "data": obj.get_data(),
                "confirmado": obj.get_confirmado(),
                "serviço": servico.get_descricao() if servico else None,
                "profissional": profissional.get_nome() if profissional else None,
                "pagamento": info_pagamento
            })

        if dic:
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhum serviço cadastrado ainda.")
