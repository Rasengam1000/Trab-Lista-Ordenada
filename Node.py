class Node:
    def __init__(self, identificador, valor, prox):
        self.__valor = valor
        self.__identificador = int(identificador)
        self.__prox = prox

    @property
    def identificador(self):
        return self.__identificador

    @property
    def prox(self):
        return self.__prox
        
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @prox.setter
    def prox(self, prox):
        self.__prox = prox

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador
