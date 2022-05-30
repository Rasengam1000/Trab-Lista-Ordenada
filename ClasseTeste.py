from ListaOrdenada import ListaOrdenada


class ClasseTeste:
    def __init__(self):
        self.lista_ordernada1 = ListaOrdenada()
        self.lista_ordernada2 = ListaOrdenada()


    def menu(self):
        while True:
            menu = int(input("Selecione a Lista desejada: \n"
                             "0 - Voltar \n1 - Lista 1 \n2 - Lista 2 \n"))
            
            if menu == 0:
                break

            while True:
                lista = self.lista_ordernada1 if menu == 1 else self.lista_ordernada2
        
                menu2 = int(input("Selecione a opção desejada: \n"
                                "0 - Voltar \n1 - Inserir Ordenado \n2 - Buscar por ID\n3 - Excluir por ID \n"))
                
                if menu2 == 0:
                    break

                elif menu2 == 1:
                    valor, identificador = input("Insira o Valor e o Identificador (numérico) separados por 1 espaço: ").split()
                    lista.InserirOrdenado(valor, int(identificador))
                
                elif menu2 == 2:
                    identificador = input("Insira o Identificador (numérico): ")
                    lista.acessar_referencia(int(identificador))

                elif menu2 == 3:
                    identificador = input("Insira o Identificador (numérico): ")
                    elemento_excluido = lista.excluir_elemento(int(identificador))
                    print(elemento_excluido.identificador, elemento_excluido.valor)
                    
                elif menu2 == 4:
                    self.iterar(1)
                elif menu2 == 5:
                    self.iterar(2)


    def pre_feito(self):
        self.lista_ordernada1.InserirOrdenado("Joao", 10)
        self.lista_ordernada1.InserirOrdenado("Marcio", 2)
        self.lista_ordernada1.InserirOrdenado("Pedro", 1)
        self.lista_ordernada1.InserirOrdenado("Lucas", 3)
        self.lista_ordernada1.InserirOrdenado("Luca", 3)
        self.lista_ordernada1.InserirOrdenado("Jose", 4)
        self.lista_ordernada1.InserirOrdenado("Luiz", 7)
        self.lista_ordernada1.InserirOrdenado("Roca", 524893)

        self.iterar(1)

        self.lista_ordernada2.InserirOrdenado("Joao", 10)
        self.lista_ordernada2.InserirOrdenado("Marcio", -15)
        self.lista_ordernada2.InserirOrdenado("Pedro", 0)
        self.lista_ordernada2.InserirOrdenado("Lucas", 75)
        self.lista_ordernada2.InserirOrdenado("Luca", 39)
        self.lista_ordernada2.InserirOrdenado("Jose", 4)
        self.lista_ordernada2.InserirOrdenado("Luiz", 4)
        self.lista_ordernada2.InserirOrdenado("Roca", 1254877)

        self.iterar(2)



    def iterar(self, lista):
        try:
            if lista == 1:
                print("")
                print(f"Primeiro: {self.lista_ordernada1.primeiro.valor}, Ultimo: {self.lista_ordernada1.ultimo.valor}")
                if self.lista_ordernada1.primeiro != None:
                    atual = self.lista_ordernada1.primeiro

                    while True:
                        print(f"ID: {atual.identificador} / Valor: {atual.valor} ({atual}, {atual.prox})")

                        if atual.prox == None:
                            break

                        atual = atual.prox
                print("")
                    
            else:
                print(f"Primeiro: {self.lista_ordernada2.primeiro.valor}, Ultimo: {self.lista_ordernada2.ultimo.valor}")
                if self.lista_ordernada2.primeiro != None:
                    atual = self.lista_ordernada2.primeiro

                    while True:
                        print(f"ID: {atual.identificador} / Valor: {atual.valor} ({atual}, {atual.prox})")

                        if atual.prox == None:
                            break

                        atual = atual.prox
                print("")
        except:
            print("Listas Vazias")



teste = ClasseTeste()

teste.pre_feito()
#teste.menu()