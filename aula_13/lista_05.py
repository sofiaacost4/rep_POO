from datetime import datetime
class Paciente:
    def __init__(self, no, c, t, na):
        self.__nome = no
        self.__cpf = c
        self.__telefone = t
        self.__nascim = na
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_nascim(self):
        return self.__nascim
    def __str__(self):
        return f"Nome: {self.__nome} - Cpf: {self.__cpf} - Telefone: {self.__telefone} - Data de Nascimento: {self.__nascim}"
    
class PacienteUI:
    __pacientes = []
    @classmethod
    def main(cls):
           op = 0
           while op != 6:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.idade()
            if op == 3: PacienteUI.alterar()
            if op == 4: PacienteUI.recuperar()
            if op == 5: PacienteUI.listar()
    @classmethod
    def menu(cls):
        print("1 - Inserir dados | 2 - Idade do paciente | 3 - Alterar dados | 4 - Recuperar dados | 5 - Listar | 6 - Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        nome = input("Nome do paciente: ")
        cpf = (input("Cpf do paciente: "))
        telefone = (input("Telefone do paciente: "))
        nascimento = input("Data de nascimento do paciente: ")
        dn = datetime.strptime(nascimento, "%d/%m/%Y")
        P = Paciente(nome, cpf, telefone, dn)
        cls.__pacientes.append(P)
    @classmethod
    def listar(cls):
        for p in cls.__pacientes:
            print(p)
    @classmethod
    def idade(cls):
        cpf = input("Qual é o cpf da pessoa que deseja saber a idade? ")
        for c in cls.__pacientes:
            if c.get_cpf() == cpf:
                print(cpf)
                hj = datetime.now()
                i = hj - c.get_nascim()
                anos = (i.days // 365)
                meses = (i.days % 365 // 30)
                print(f"Idade de {c.get_nome()}: {anos} anos e {meses} meses.")
                return
            print("Cpf não encontrado.")
    @classmethod
    def alterar(cls):
        pass
    @classmethod
    def recuperar(cls):
        pass
PacienteUI.main()