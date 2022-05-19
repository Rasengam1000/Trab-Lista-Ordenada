from Node import Node


class Lista_ordenada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    def InserirOrdenado(self, valor):
        if self.__primeiro != None:
            if valor > self.__ultimo.valor:
                self.__ultimo.prox = Node(valor, None)
                return
            
        
            atual = self.__primeiro
            antigo = None
            while True:
                if valor < atual.valor:
                    if antigo == None:
                        print("a")
                        self.__primeiro = Node(valor, atual)

                    else:
                        print("b")
                        antigo.prox = Node(valor, atual)
                        
                else:
                    atual.prox = Node(valor, atual.prox)
                if atual.prox == None:
                    break
                antigo = atual
                atual = atual.prox 
        else:
            self.__primeiro = Node(valor, None)
            self.__ultimo = self.__primeiro
       


 #       self.inserir_posiçao(pos)
#-  Excluir ( ID do elemento a ser excluído)
#- (elemento) Buscar ( ID do elemento procurado)



    def inserir_posiçao(self, pos, valor):
        if self.__primeiro != None:
            atual = self.__primeiro
            if pos == 0:
                if self.__primeiro.prox == None:
                    self.__ultimo = self.__primeiro
                    self.__primeiro = Node(valor, self.__primeiro)
                else:
                    self.__primeiro = Node(valor, self.__primeiro)

            elif pos == -1:
                self.__ultimo.prox = Node(valor, None)
                self.__ultimo = self.__ultimo.prox
            
            else:
                atual = self.__primeiro
                antigo = None
                for i in range(0, pos + 1):
                    if i == pos:
                        if atual.prox == None:
                            atual.prox = Node(valor, None)
                            self.__ultimo = atual.prox
                            break
                        else:
                            antigo.prox = Node(valor, atual)
                            break

                    antigo = atual
                    atual = atual.prox
                    
    def excluir_posiçao(self, pos):
        if pos == 0:
            self.__primeiro = self.__primeiro.prox

        else:
            atual = self.__primeiro
            for i in range(pos):
                if atual.prox == None:
                    return

                antigo = atual
                atual = atual.prox

            antigo.prox = atual.prox
            
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

    def excluir_elemento(self, valor):
        if self.__primeiro != None:
            atual = self.__primeiro
            antigo = None
            while True:
                if atual.valor == valor:
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

    def acessar_referencia(self, valor):
        atual = self.__primeiro
        while True:
            if atual.valor == valor:
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
        print(self.__primeiro.valor, self.__ultimo.valor)
        if self.__primeiro != None:
            atual = self.__primeiro
            while True:
                print(f"{atual.valor} ({atual}, {atual.prox})", end=", ")
                if atual.prox == None:
                    break
                atual = atual.prox

lista = Lista_ordenada()

lista.InserirOrdenado(1)
lista.InserirOrdenado(0)
lista.InserirOrdenado(3)
#lista.InserirOrdenado(2)
lista.InserirOrdenado(-1)
lista.InserirOrdenado(4)
lista.InserirOrdenado(5)

lista.iterar()