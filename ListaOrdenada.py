from Node import Node
from ListaEncadeada import ListaEncadeada


class ListaOrdenada(ListaEncadeada):
    def __init__(self):
        super().__init__()


    def inserir_ordenado(self, valor, identificador):
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

    def excluir_elemento(self, identificador):      
        super().excluir_elemento(identificador)
    
    def acessar_referencia(self, identificador):
        super().acessar_referencia(identificador)


#lista = ListaOrdenada()

#lista.inserir_ordenado("Marcio", 2)
#lista.inserir_ordenado("Pedro", 1)
#lista.inserir_ordenado("Lucas", 3)
#lista.inserir_ordenado("Jose", 4)
#lista.inserir_ordenado("Joao", 3)
#lista.inserir_ordenado("Luiz", 15888888)
#lista.inserir_ordenado("Roca", 3)

#lista.iterar()