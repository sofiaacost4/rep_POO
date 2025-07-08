from datetime import datetime
from enum import Enum

class Dias(Enum):
    Segunda = 0
    Terça = 1
    Quarta = 2
    Quinta = 3
    Sexta = 4
    Sábado = 5
    Domingo = 6

x = datetime(2025, 7, 8)
print(x)
print(type(x))
hoje = datetime.now()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(Dias(hoje.weekday()))
d = input("Informe sua data de nascimento: ")
dn = datetime.strptime(d, "%d/%m/%Y")
print(d, type(d))
print(dn, type(dn))

dv = hoje - dn
print(dv)
print(type(dv))
print(dv.days // 365, "anos")
print(dv.days % 365 // 30, "meses")
print(dv.days % 365 % 30, "dias")