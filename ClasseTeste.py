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
                    lista.inserir_ordenado(valor, int(identificador))
                
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
        self.lista_ordernada1.inserir_ordenado("Joao", 10)
        self.lista_ordernada1.inserir_ordenado("Marcio", 2)
        self.lista_ordernada1.inserir_ordenado("Pedro", 1)
        self.lista_ordernada1.inserir_ordenado("Lucas", 3)
        self.lista_ordernada1.inserir_ordenado("Luca", 3)
        self.lista_ordernada1.inserir_ordenado("Jose", 4)
        self.lista_ordernada1.inserir_ordenado("Luiz", 7)
        self.lista_ordernada1.inserir_ordenado("Roca", 524893)

        self.iterar(1)

        self.lista_ordernada2.inserir_ordenado("Joao", 10)
        self.lista_ordernada2.inserir_ordenado("Marcio", -15)
        self.lista_ordernada2.inserir_ordenado("Pedro", 0)
        self.lista_ordernada2.inserir_ordenado("Lucas", 75)
        self.lista_ordernada2.inserir_ordenado("Luca", 39)
        self.lista_ordernada2.inserir_ordenado("Jose", 4)
        self.lista_ordernada2.inserir_ordenado("Luiz", 4)
        self.lista_ordernada2.inserir_ordenado("Roca", 1254877)

        self.iterar(2)



    def iterar(self, lista):
        print("")
        try:
            if lista == 1:
                self.lista_ordernada1.iterar()
                    
            else:
                self.lista_ordernada2.iterar()

            print("")

        except:
            print("Listas Vazias")


#teste = ClasseTeste()

#teste.pre_feito()
#teste.menu()