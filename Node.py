class Node:
    def __init__(self, valor, prox):
        self.__valor = valor
        self.__prox = prox

    @property
    def valor(self):
        return self.__valor

    @property
    def prox (self):
        return self.__prox

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @prox.setter
    def prox (self, prox):
        self.__prox = prox

