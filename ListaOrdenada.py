from Node import Node
from ListaEncadeada import ListaEncadeada


class ListaOrdenada(ListaEncadeada):
    def __init__(self):
        super().__init__()


    def InserirOrdenado(self, valor, identificador):
        if self.primeiro == None:
            self.inserir_primeiro(valor, identificador)

        else:
            if identificador > self.ultimo.identificador:
                self.inserir_ultimo(valor, identificador)
                return

            else:
                atual = self.primeiro
                antigo = None
                while True:
                    if identificador < atual.identificador:
                        if antigo == None:
                            self.primeiro = Node(identificador, valor, atual)

                        else:
                            antigo.prox = Node(identificador, valor, atual)

                        break

                    if atual.prox == None or identificador == atual.identificador:
                        break
                    
                    antigo = atual
                    atual = atual.prox 



lista = ListaOrdenada()

lista.InserirOrdenado("Marcio", 2)
lista.InserirOrdenado("Pedro", 1)
lista.InserirOrdenado("Lucas", 3)
lista.InserirOrdenado("Jose", 4)
lista.InserirOrdenado("Joao", 3)
lista.InserirOrdenado("Luiz", 15888888)
lista.InserirOrdenado("Roca", 3)

lista.iterar()