from datetime import datetime, timedelta
import json
from models.dao import DAO

class Pagamento:
    def __init__(self, id, id_horario, valor_total, parcelas_totais, parcelas_escolhidas, parcelas_pagas, valor_parcela, estado, data_ultima_parcela=None):
        self.set_id(id)
        self.set_id_horario(id_horario)
        self.set_valor_total(valor_total)
        self.set_parcelas_totais(parcelas_totais)
        self.set_parcelas_escolhidas(parcelas_escolhidas)
        self.set_parcelas_pagas(parcelas_pagas)
        self.set_valor_parcela(valor_parcela)
        self.set_estado(estado)
        self.__data_ultima_parcela = data_ultima_parcela or datetime.now()

    def get_id(self): return self.__id
    def get_id_horario(self): return self.__id_horario
    def get_valor_total(self): return self.__valor_total
    def get_parcelas_totais(self): return self.__parcelas_totais
    def get_parcelas_escolhidas(self): return self.__parcelas_escolhidas
    def get_parcelas_pagas(self): return self.__parcelas_pagas
    def get_valor_parcela(self): return self.__valor_parcela
    def get_estado(self): return self.__estado
    def get_data_ultima_parcela(self): return self.__data_ultima_parcela

    def set_id(self, id): self.__id = id
    def set_id_horario(self, id_horario): self.__id_horario = id_horario
    def set_valor_total(self, valor_total): self.__valor_total = valor_total
    def set_parcelas_totais(self, parcelas_totais): self.__parcelas_totais = parcelas_totais
    def set_parcelas_escolhidas(self, parcelas_escolhidas): self.__parcelas_escolhidas = parcelas_escolhidas
    def set_parcelas_pagas(self, parcelas_pagas): self.__parcelas_pagas = parcelas_pagas
    def set_valor_parcela(self, valor_parcela): self.__valor_parcela = valor_parcela
    def set_estado(self, estado): self.__estado = estado
    def set_data_ultima_parcela(self, data): self.__data_ultima_parcela = data

    def atualizar_parcelas(self):
        if self.__estado == "Pago":
            return False
        agora = datetime.now()
        diferenca = agora - self.__data_ultima_parcela
        if diferenca.days >= 30 and self.__parcelas_pagas < self.__parcelas_escolhidas:
            self.__parcelas_pagas += 1
            self.__data_ultima_parcela = agora
            if self.__parcelas_pagas >= self.__parcelas_escolhidas: self.__estado = "Pago"
            else: self.__estado = "Pago parcialmente"
            return True
        return False
    
    def pagar_parcela(self):
        from datetime import datetime
        if self.__estado == "Pago":
            raise ValueError("Este serviço já foi pago.")
        if self.__parcelas_pagas < self.__parcelas_escolhidas:
            self.__parcelas_pagas += 1
            self.__data_ultima_parcela = datetime.now().strftime("%d/%m/%Y %H:%M")
            if self.__parcelas_pagas == self.__parcelas_escolhidas:
                self.__estado = "Pago"
            else:
                self.__estado = "Pago parcialmente"
        else: raise ValueError("Todas as parcelas já foram pagas.")

    def to_json(self):
        if isinstance(self.__data_ultima_parcela, str):
            self.__data_ultima_parcela = self.__data_ultima_parcela
        else:
            self.__data_ultima_parcela = self.__data_ultima_parcela.strftime("%d/%m/%Y %H:%M")
        return {
            "id": self.__id,
            "id_horario": self.__id_horario,
            "valor_total": self.__valor_total,
            "parcelas_totais": self.__parcelas_totais,
            "parcelas_escolhidas": self.__parcelas_escolhidas,
            "parcelas_pagas": self.__parcelas_pagas,
            "valor_parcela": self.__valor_parcela,
            "estado": self.__estado,
            "data_ultima_parcela": self.__data_ultima_parcela
        }

    @staticmethod
    def from_json(dic):
        data = dic.get("data_ultima_parcela")
        if data:
            data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        return Pagamento(
            dic["id"],
            dic["id_horario"],
            dic["valor_total"],
            dic.get("parcelas_totais", 1),
            dic.get("parcelas_escolhidas", 1),
            dic.get("parcelas_pagas", 0),
            dic.get("valor_parcela", 0),
            dic.get("estado", "Pendente"),
            data
        )

class PagamentoDAO(DAO):

    @classmethod
    def listar_por_horario(cls, id_horario):
        cls.abrir()
        for p in cls._objetos:
            if p.get_id_horario() == id_horario:
                return p
        return None

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("pagamentos.json", "r") as arquivo:
                lista_dic = json.load(arquivo)
                for dic in lista_dic:
                    cls._objetos.append(Pagamento.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("pagamentos.json", "w") as arquivo:
            json.dump(cls._objetos, arquivo, default=lambda p: p.to_json())
