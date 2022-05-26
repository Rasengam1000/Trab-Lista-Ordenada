class Node:
    def __init__(self, nome, cpf, prox):
        self.__nome = nome
        self.__cpf = int(cpf)
        self.__prox = prox

    @property
    def cpf(self):
        return self.__cpf

    @property
    def prox (self):
        return self.__prox
        
    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @prox.setter
    def prox (self, prox):
        self.__prox = prox

    @cpf.setter
    def cpf (self, cpf):
        self.__cpf = cpf
