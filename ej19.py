
class Nodo:
    def __init__(self, valor):
        self.valor = valor  
        self.siguiente = None  


nodo1 = Nodo("pepe")
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)


nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5


def imprimir_lista(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.siguiente


imprimir_lista(nodo1)
