from datetime import datetime
from enum import Enum
class Pagamento(Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2
class Boleto:
    def __init__(self, c, dE, dV, dP, vB, vP):
        self.__codigo = c
        self.__dtEmissao = dE
        self.__dtVencimento = dV
        self.__dtPago = dP
        self.__vBoleto = vB
        self.__vPago = 0
        self.__situacao = Pagamento.EmAberto
    def pagar(self, valorpago):
        if valorpago == self.__vBoleto:
            return Pagamento.Pago
        if valorpago != 0 and valorpago < self.__vBoleto:
            return Pagamento.PagoParcial
    def situacao(self):
        return self.__situacao


    def __str__(self):
        return f"Código de barras: {self.__codigo} - Data de emissão: {self.__dtEmissao} - Data de vencimento: {self.__dtVencimento} - Data de pagamento: {self.__dtPago} - Valor do boleto: {self.__vBoleto} - Valor pago: {self.__vPago} - Situação do pagamento: {Boleto.situacao()}"

class BoletoUI:
    @classmethod
    def menu(cls):
        op = int(input("1 - Inserir dados | 2 - Situação | 3 - Pagar | 4 - Alterar | 5 - Recuperar | 6 - Fim"))