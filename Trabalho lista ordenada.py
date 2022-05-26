from Node import Node

 #  inserir odenado self.inserir_posiçao(pos)
#-  Excluir ( ID do elemento a ser excluído)
#- (elemento) Buscar ( ID do elemento procurado)
# OK


class ListaOrdenada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    def InserirOrdenado(self, nome, cpf):
        if self.__primeiro != None:
            if cpf > self.__ultimo.cpf:
                self.__ultimo.prox = Node(nome, cpf, None)
                self.__ultimo = self.__ultimo.prox
                return

        
            atual = self.__primeiro
            antigo = None
            while True:
                if cpf < atual.cpf:
                    if antigo == None:
                        self.__primeiro = Node(nome, cpf, atual)
                        break

                    else:
                        antigo.prox = Node(nome, cpf, atual)
                        break

                elif cpf == atual.cpf:
                    break

                if atual.prox == None:
                    break
                
                antigo = atual
                atual = atual.prox 
        else:
            self.__primeiro = Node(nome, cpf, None)
            self.__ultimo = self.__primeiro

    
    def excluir_cpf(self, cpf):
        if self.__primeiro != None:
            atual = self.__primeiro
            antigo = None
            while True:
                if atual.cpf == cpf:
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

    def acessar_referencia(self, nome):
        atual = self.__primeiro
        while True:
            if atual.nome == nome:
                return atual

            if atual.prox == None:
                break

            atual = atual.prox 

    def acessar_posiçao(self, pos):
        atual = self.__primeiro
        for i in range(pos+1):
            if i == pos:
                return atual

            if atual.prox == None:
                break

            atual = atual.prox 

    def acessar_primeiro(self):
        return self.__primeiro

    def iterar(self):
        print(self.__primeiro.nome, self.__ultimo.nome)
        if self.__primeiro != None:
            atual = self.__primeiro
            while True:
                print(f"{atual.nome}, ' CPF: ', {atual.cpf}, ({atual}, {atual.prox})", end=", ")
                if atual.prox == None:
                    break
                atual = atual.prox

lista = ListaOrdenada()

lista.InserirOrdenado("Pedro", 1)
lista.InserirOrdenado("Marcio", 2)
lista.InserirOrdenado("Lucas", 3)
lista.InserirOrdenado("Jose", 4)
lista.InserirOrdenado("Joao", 3)
lista.excluir_primeiro()
lista.excluir_ultimo()
lista.InserirOrdenado("De Lucca", 10)
lista.excluir_cpf(3)

lista.iterar()