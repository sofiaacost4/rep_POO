import json
x = [10, 5, 8, 4]
print(type(x))
x[0] = 3
print(x)

x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}

for item in x.items(): print(item, type(item))
a = (5, 8, 10)
b = [5, 8 , 10]
c = {0 : 5, 1 : 8, 2 : 10}
print(type(a))
print(type(b))
print(type(c))
print(type(x))

print(x["RN"])

x["AM"] = "Manaus"
x["PB"] = "J. Pessoa"

print(x)
print(*x)
print(max(x))
print(min(x))

class Cliente:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
    def __str__(self):
        return f"Id: {self.__id} - Nome: {self.__nome}"
def salvar():
    a = Cliente(1, "Alex")
    b = Cliente(2, "Daniele")
    x = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(x, arquivo, default = vars)
    #arquivo.close()
def abrir():
    x = []
    with open("clientes.json", mode="r") as arquivo:
        lista = json.load(arquivo)
        for dic in lista:
            c = Cliente(dic["id"], dic["nome"])
            x.append(c)
    for c in x: print(c)

abrir()
