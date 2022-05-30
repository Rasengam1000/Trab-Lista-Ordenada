from Node import Node


class ListaEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self):
        return self.__ultimo

    @primeiro.setter
    def primeiro(self, primeiro):
        self.__primeiro = primeiro

    @ultimo.setter
    def ultimo(self, ultimo):
        self.__ultimo = ultimo


    def inserir_primeiro(self, valor, identificador):
        if self.__primeiro == None:
            self.__primeiro = Node(identificador, valor, None)
            self.__ultimo = self.__primeiro
        elif self.__primeiro.prox == None:
            self.__ultimo = self.__primeiro
            self.__primeiro = Node(identificador, valor, self.__primeiro)
        else:
            self.__primeiro = Node(identificador, valor, self.__primeiro)

    def inserir_ultimo(self, valor, identificador):
        if self.__ultimo == None:
            self.__primeiro = Node(identificador, valor, None)
            self.__ultimo = self.__primeiro
        elif self.__primeiro.prox == None:
            self.__ultimo = Node(identificador, valor, None)
            self.__primeiro.prox = self.__ultimo
        else:
            self.__ultimo.prox = Node(identificador, valor, None)
            self.__ultimo = self.__ultimo.prox

            
    def excluir_primeiro(self):
        if self.__primeiro != None:
            self.__primeiro = self.__primeiro.prox

    def excluir_ultimo(self):
        if self.__primeiro != None:
            atual = self.__primeiro
            while True:
                if atual.prox == self.__ultimo:
                    atual.prox = None
                    self.__ultimo = atual
                    break

                atual = atual.prox

    def excluir_elemento(self, identificador):
        if self.__primeiro != None:
            atual = self.__primeiro
            antigo = None
            while True:
                if atual.identificador == identificador:
                    if antigo == None:
                        self.__primeiro = atual.prox
                    elif atual.prox == None:
                        antigo.prox = None
                        self.__ultimo = antigo
                    else:
                        antigo.prox = atual.prox

                    return
                        

                if atual.prox == None:
                    return

                antigo = atual
                atual = atual.prox

    def acessar_referencia(self, identificador):
        atual = self.__primeiro
        while True:
            if atual.identificador == identificador:
                return atual

            if atual.prox == None:
                break

            atual = atual.prox 

    def acessar_primeiro(self):
        return self.__primeiro

    def iterar(self):
        print(f"Primeiro: {self.__primeiro.valor}, Ultimo: {self.__ultimo.valor}")
        if self.__primeiro != None:
            atual = self.__primeiro

            while True:
                print(f"ID: {atual.identificador} / Valor: {atual.valor} ({atual}, {atual.prox})")

                if atual.prox == None:
                    break

                atual = atual.prox

#lista = ListaEncadeada()

#lista.inserir_primeiro(1)
#lista.inserir_primeiro(2)
#lista.inserir_primeiro(3)
#lista.inserir_ultimo(4)
#lista.inserir_ultimo(5)
#lista.iterar()
#lista.excluir_elemento(1)
#lista.excluir_primeiro()
#lista.excluir_ultimo()
#lista.excluir_ultimo()

#print(lista.acessar_posiçao(1).valor)
#lista.iterar()
